---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- PostgreSQL
- pgRouting
- 图数据库
- 算法
- 数据库优化
title: 将 Postgres 用作图数据库：巧妙（或超常）运用 pgRouting
---
### 文章背景与核心概要

本文探讨了 pgRouting 这一强大的 Postgres 扩展。通常情况下，它与 PostGIS 结合用于地理空间路由。然而除了寻找最短地理路径之外，pgRouting 还可以作为专用图数据库（如 Neo4j）或专用图扩展（如 Apache AGE）的轻量级、灵活替代方案。

通过对抽象系统进行建模——例如任务依赖关系、网络延迟和推荐系统——开发人员可以直接在 PostgreSQL 中利用内置的图算法（如 Dijkstra 和 A*）。本文通过任务调度、服务器路由和推荐系统等实际案例，展示了如何在非 GIS 场景下充分挖掘 pgRouting 的巨大潜力。

---

## 什么是 pgRouting？

[pgRouting](https://github.com/pgRouting/pgrouting) 是 PostGIS 的一个扩展，提供了地理空间路由功能。你可以使用它来计算最短路径、执行网络分析以及在基于图的结构上解决复杂的路由问题。最常见的情况是，它被用于地理信息系统（GIS）中，以确定两个地点之间的最快路线等任务。

> [pgRouting](https://github.com/pgRouting/pgrouting) is an extension of PostGIS that provides geospatial routing functionality. You can use it to calculate the shortest path, perform network analysis, and solve complex routing problems on a graph-based structure. Most commonly, this is used in Geographic Information Systems (GIS) for tasks like determining the fastest route between two locations.

---

## 处理图数据

pgRouting 的强大之处在于它能够处理任何结构化为图的数据。图本质上是一个由互相连接的点构成的网络，其中：

* **节点（Nodes）**代表实体。
* **边（Edges）**代表这些节点之间的关系或路径。

在地图/[GIS](https://en.wikipedia.org/wiki/Geographic_information_system)中，节点和边分别代表交叉路口和道路。然而，这种结构也可以应用于抽象系统，例如社交网络（其中用户是节点，友谊是边）。

> The power of pgRouting lies in its ability to work with any data structured as a graph. A graph is essentially a network of interconnected points, where:
> 
> * **Nodes** represent entities.
> * **Edges** represent relationships or paths between those nodes.
> 
> In maps / [GIS](https://en.wikipedia.org/wiki/Geographic_information_system), nodes and edges represent intersections and roads respectively. However, this structure can also be applied to abstract systems like a social networks, where users are nodes and friendships are edges.

---

## pgRouting 的非 GIS 用例

让我们探讨一下 pgRouting 如何应用于一些非 [GIS](https://en.wikipedia.org/wiki/Geographic_information_system) 问题。

> Let's explore how pgRouting can be applied to a few non-[GIS](https://en.wikipedia.org/wiki/Geographic_information_system) problems.

### 任务调度

在任何项目中，任务之间都存在依赖关系。例如，任务 B 只能在任务 A 完成后开始。这就创建了一个[有向无环图（Directed Acyclic Graph）](https://en.wikipedia.org/wiki/Directed_acyclic_graph)，其中：

* 节点代表任务
* 边代表依赖关系

管理项目最具挑战性的方面之一是确定“关键路径”（Critical Path）——由最长的依赖序列决定的项目总体持续时间。

使用 pgRouting，你可以对任务的依赖关系进行建模，并使用图算法来寻找关键路径。假设我们有一个表 `tasks`，其中任务依赖关系被建模为一个图：

> In any project, tasks have dependencies. For example, task B can only start after task A is completed. This creates a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph), where:
> 
> * nodes represent tasks
> * edges represent dependencies
> 
> One of the most challenging aspects of managing projects is determining the “critical path” — the project's overall duration, determined by the longest sequence of dependencies.
> 
> Using pgRouting, you can model your task's dependencies, using graph algorithms to find the critical path. Suppose we have a table `tasks` with task dependencies modeled as a graph:

```sql
-- Create the tasks table with dependencies
create table tasks (
  id serial primary key,
  name text not null
);

-- insert tasks into the table
insert into tasks (name)
values
  ('Start Project'),
  ('Task A'),
  ('Task B'),
  ('Task C'),
  ('Task D'),
  ('End Project');

-- create the dependencies table
create table dependencies (
  id serial primary key,
  source integer not null, -- task id where the dependency starts
  target integer not null, -- task id where the dependency ends
  duration integer not null, -- duration of the task in days
  constraint fk_source foreign key (source) references tasks (id),
  constraint fk_target foreign key (target) references tasks (id)
);

-- insert dependencies with durations (directed edges)
insert into dependencies (source, target, duration)
values
  (1, 2, 3), -- start project -> task a (3 days)
  (2, 3, 4), -- task a -> task b (4 days)
  (3, 4, 5), -- task b -> task c (5 days)
  (4, 5, 2), -- task c -> task d (2 days)
  (5, 6, 6); -- task d -> end project (6 days)
```

然后你可以使用 [`pgr_dijkstra()`](https://docs.pgrouting.org/latest/en/pgr_dijkstra.html) 函数来查找穿过这些任务的最短（或最长）路径，从而有效地规划出项目进度表：

> You can then use the [`pgr_dijkstra()`](https://docs.pgrouting.org/latest/en/pgr_dijkstra.html) function to find the shortest (or longest) path through the tasks, allowing you to map out the project schedule effectively:

```sql
create schema if not exists extensions;
create extension pgrouting schema extensions cascade;

-- find the longest path using pgr_dijkstra()
-- (as it calculates shortest path, use negative weights)
select * FROM extensions.pgr_dijkstra(
    'select id, source, target, duration as cost from dependencies',
    1,  -- Start Project (Task ID 1)
    6   -- End Project (Task ID 6)
);
```

这将返回一个表格，显示该项目从开始到结束需要 20 天：

> This returns a table showing that this project will take 20 days from start to finish:

| **seq** | **path_seq** | **node** | **edge** | **cost** | **agg_cost** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 1 | 1 | 3 | 0 |
| 2 | 2 | 2 | 2 | 4 | 3 |
| 3 | 3 | 3 | 3 | 5 | 7 |
| 4 | 4 | 4 | 4 | 2 | 12 |
| 5 | 5 | 5 | 5 | 6 | 14 |
| 6 | 6 | 6 | -1 | 0 | 20 |

<details>
<summary>延伸阅读：Dijkstra 算法</summary>

`pgr_dijkstra()` 函数实现了 [Dijkstra 算法](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)，该算法用于寻找图中节点之间的最短路径。根据连接节点的边的成本，该算法可保证从源节点到目标节点（或所有其他节点）的最短路径。

趣闻：Dijkstra 算法由荷兰计算机科学家 Edsger Dijkstra 于 1959 年发表。它是一个“贪婪”算法，意味着它总是选择接下来要探索的最近、最便宜的节点。

</details>

> <details>
> <summary>Tangent: the Dijkstra algorithm</summary>
> 
> The `pgr_dijkstra()` function implements [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm), which is used to find the shortest path between nodes in a graph. This algorithm guarantees the shortest path from a source node to a target node (or all other nodes), based on the cost of edges connecting the nodes.
> 
> Fun fact: Dijkstra's algorithm was published in 1959 by Dutch computer scientist Edsger Dijkstra. It's a “greedy” algorithm, meaning it always picks the closest, cheapest node to explore next.
> 
> </details>

### 基于资源分配的反向代理路由

分布式系统通常涉及在节点网络中高效分配资源。每个节点可以代表一个物理位置或计算进程，而边则代表在它们之间移动资源的可用通路。例如，在云基础设施中，pgRouting 可以通过寻找路由数据的最短或拥堵最少的路径，来帮助确定如何在分布式服务器集群中分配计算任务。

假设你有一个由节点表示的服务器网络，它们的数据库连接在 `servers` 表中表示为边。

> Distributed systems usually involve allocating resources efficiently across a network of nodes. Each node might represent a physical location or a computing process, and the edges represent the available pathways to move resources between them. For example, in a cloud infrastructure, pgRouting could help determine how to allocate compute tasks across a set of distributed servers by finding the shortest or least-congested path to route data.
> 
> Suppose you have a network of servers represented by nodes and their data connections as edges in a table `servers`.

```sql
-- create the servers table representing the nodes
create table servers (
  id serial primary key,
  name text,
  x double precision, -- x coordinate for spatial data (latitude)
  y double precision -- y coordinate for spatial data (longitude)
);

-- insert some sample servers
insert into servers (name, x, y)
values
  ('server a', 0, 0),
  ('server b', 2, 1),
  ('server c', 4, 3),
  ('server d', 3, 5);

-- create the server_connections table representing the edges
create table server_latency (
  id serial primary key,
  source integer,
  target integer,
  cost double precision, -- cost could represent latency or bandwidth
  x1 double precision, -- x coordinate of source
  y1 double precision, -- y coordinate of source
  x2 double precision, -- x coordinate of target
  y2 double precision, -- y coordinate of target,
  constraint fk_source foreign key (source) references servers (id),
  constraint fk_target foreign key (target) references servers (id)
);

-- insert connections between servers
insert into server_latency (source, target, cost, x1, y1, x2, y2)
values
  (1, 2, 1.5, 0, 0, 2, 1), -- server a -> server b with a cost of 1.5 (could be latency)
  (2, 3, 2.0, 2, 1, 4, 3), -- server b -> server c with a cost of 2.0
  (2, 4, 1.8, 2, 1, 3, 5), -- server b -> server d with a cost of 1.8
  (4, 3, 1.0, 3, 5, 4, 3); -- server d -> server c with a cost of 1.0
```

然后你可以使用 [`pgr_astar`](https://docs.pgrouting.org/latest/en/pgr_aStar.html)() 来寻找数据或计算任务在该网络中穿梭最高效的路径，从而优化速度或负载：

> You can then use [`pgr_astar`](https://docs.pgrouting.org/latest/en/pgr_aStar.html)() to find the most efficient path for data or compute tasks to travel through this network, optimizing for speed or load:

```sql
-- Query to find the most efficient path (using pgr_astar)
select *
from
  extensions.pgr_astar(
    'select id, source, target, cost, x1, y1, x2, y2 from server_latency',
    1,
    3 -- Start from Server A (id=1) to Server C (id=3)
  );
```

<details>
<summary>延伸阅读：A* 算法</summary>

`pgr_astar()` 函数是 [A* (A-star) 算法](https://en.wikipedia.org/wiki/A*_search_algorithm)的实现。它用于在图中的两点之间寻找最有效（最短）的路径。A* 常用于导航和路由，因为在许多场景下它比 Dijkstra 算法更高效，特别是当你拥有带坐标的空间数据（例如 X、Y 位置）时。

趣闻：A* 最初是为 20 世纪 60 年代的应用程序以及游戏中的寻路而设计的。如今，它是视频游戏开发中最广泛使用的算法之一，可帮助角色在复杂环境中高效导航。

</details>

> <details>
> <summary>Tangent: the A* algorithm</summary>
> 
> The `pgr_astar()` function is an implementation of the [A* (A-star) algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm). It's used to find the most efficient (shortest) path between two points in a graph. A* is commonly used in navigation and routing because it is more efficient than Dijkstra's algorithm in many scenarios, especially when you have spatial data with coordinates (e.g., X, Y positions).
> 
> Fun fact: A* was originally designed in the 1960s for artificial intelligence applications and pathfinding in games. Today, it's one of the most widely used algorithms in video game development to help characters navigate complex environments efficiently.
> 
> </details>

### 类似 YouTube 的推荐系统

在使用知识图谱的推荐系统或搜索算法中，pgRouting 可用于建立实体和事件之间的关系。以 YouTube 的推荐算法为例，我们可以将这些数据构造成一个图，其中：

* **节点**代表用户、视频或分类等实体。
* **边**代表这些实体之间的关系或互动，例如用户喜欢某个视频，或者视频属于同一分类。

让我们创建一个“节点”列表：

> In recommendation engines or search algorithms that use knowledge graphs, pgRouting can be used to build relationships between entities and events. Take YouTube's recommendation algorithm, we can structure this data as a graph where:
> 
> * **Nodes** represent entities like users, videos, or categories.
> * **Edges** represent relationships or interactions between those entities, such as a user liking a video or videos being part of the same category.
> 
> Let's create a list of “nodes”:

```sql
create table categories (
  id serial primary key,
  name text
);

insert into categories (name)
values
  ('Graph Theory'),
  ('AI & Machine Learning'),
  ('Python Programming');

create table videos (
  id serial primary key,
  title text,
  category_id int references categories (id)
);

insert into videos (title, category_id)
values
  ('Intro to Graph Theory', 1),
  ('Advanced Graph Algorithms', 1),
  ('Graph Neural Networks', 2),
  ('Beginner Python Tutorial', 3),
  ('Advanced Python Techniques', 3);
```

以及一些“边”：

> And some “edges”:

```sql
create table video_relationships (
  source_video_id int references videos (id),
  target_video_id int references videos (id),
  relationship_type text, -- 'same_category', 'watched_by_same_users', etc.
  weight int default 1 -- strength of the relationship
);

insert into video_relationships (source_video_id, target_video_id, relationship_type, weight)
values
  (1, 2, 'same_category', 5), -- "Intro to Graph Theory" and "Advanced Graph Algorithms" are in the same category
  (2, 3, 'watched_by_same_users', 3), -- "Advanced Graph Algorithms" and "Graph Neural Networks" are often watched together
  (4, 5, 'same_category', 5); -- "Beginner Python Tutorial" and "Advanced Python Techniques"

create table interactions (
  user_id int references auth.users (id),
  video_id int references videos (id),
  interaction_type text, -- 'liked', 'viewed', etc.
  weight int default 1 -- strength of the interaction
);

insert into interactions (user_id, video_id, interaction_type, weight)
values
  ('user_01', 1, 'viewed', 5), -- "User 01" watched "Intro to Graph Theory" to the end (weight = 5)
  ('user_01', 2, 'liked', 5), -- "User 01" liked "Advanced Graph Algorithms"
  ('user_02', 3, 'viewed', 2), -- "User 02" watched "Graph Neural Networks" and bounced halfway through (weight = 2)
  ('user_03', 4, 'liked', 5), -- "User 03" liked "Beginner Python Tutorial"
  ('user_03', 5, 'viewed', 2); -- "User 03" watched "Advanced Python Techniques" and bounced halfway through (weight = 2)
```

现在我们可以使用 `pgr_dijkstra()` 函数来寻找用户与新视频之间最短或最相关的路径。例如，让我们结合 `user_01` 过去的互动记录，寻找与其最相关的视频：

> Now we can use the `pgr_dijkstra()` function to find the shortest or most relevant path between a user and new videos. For example, let's find videos that are most relevant to `user_01` considering their past interactions:

<details>
<summary>延伸阅读：对推荐结果进行排序</summary>

既然它“只是 Postgres”，使用 `order by` 子句对结果进行排序就变得非常简单。例如，如果我们把上面的 `pgr_dijkstra()` 结果存储在一个名为“recommendations”的表中，我们可以使用如下查询按最高排名对路径进行排序：

```sql
select videos.title, sum(weight) as recommendation_score
from
  recommendations
  join videos on recommendations.target = videos.id
group by videos.title
order by recommendation_score desc;
```

</details>

> <details>
> <summary>Tangent: ranking recommendations</summary>
> 
> Since it's “just postgres” it's simple enough to rank the results using an `order by` clause. For example, if we stored the `pgr_dijkstra()` results above in a table called “recommendations”, we use this a query like this to sort the paths by the highest ranking:
> 
> ```sql
> select videos.title, sum(weight) as recommendation_score
> from
>   recommendations
>   join videos on recommendations.target = videos.id
> group by videos.title
> order by recommendation_score desc;
> ```
> 
> </details>

---

## 开始使用

pgRouting 是 Postgres 的一个强大扩展，可用于解决广泛的基于图的问题。查看 [pgRouting 文档](https://docs.pgrouting.org/latest/en/index.html)了解更多关于如何使用它的信息。你也可以在 Supabase 上使用它：

* 文档：[pgrouting: Geospatial Routing](/docs/guides/database/extensions/pgrouting)
* 启动新的 Postgres 数据库：[database.new](https://database.new)

> ## Get Started
> 
> pgRouting is a powerful extension for Postgres that can be used to solve a wide range of graph-based problems. Check out the [pgRouting docs](https://docs.pgrouting.org/latest/en/index.html) for more information on how to use it. You can also use it on Supabase:
> 
> * Docs: [pgrouting: Geospatial Routing](/docs/guides/database/extensions/pgrouting)
> * Launch a new Postgres database: [database.new](https://database.new)