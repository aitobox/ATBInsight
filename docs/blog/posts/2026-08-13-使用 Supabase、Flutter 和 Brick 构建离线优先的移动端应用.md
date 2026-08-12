---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- Flutter
- Supabase
- 离线优先
- SQLite
- Brick
title: 使用 Supabase、Flutter 和 Brick 构建离线优先的移动端应用
---
### 文章背景与核心概要
在移动应用开发中，网络连接不稳定（如地铁、飞机或弱网环境）往往会导致应用体验大打折扣，“离线优先（Offline-First）”架构因此成为现代应用开发的黄金标准。本文介绍如何结合使用一体化数据管理器 **Brick**、云端后端 **Supabase** 以及本地缓存 **SQLite**，在 Flutter 中构建具备强大离线功能的移动应用。

文章详细梳理了从零搭建离线优先 Flutter 应用的全过程，包括依赖配置、目录结构划分、数据模型定义及代码生成。通过统一的 Repository（存储库）入口，Brick 能够自动处理本地缓存与远程服务器的数据同步、离线请求队列管理以及复杂对象关联查询。无论是应对断网重试机制还是提升弱网下的响应速度，这套经过实战检验的架构都为开发者提供了一种优雅且高效的解决方案。

---

# 使用 Supabase、Flutter 和 Brick 构建离线优先的移动端应用

> 💡 **没有时间阅读？** 直接前往 [示例代码仓库](https://github.com/GetDutchie/brick/tree/main/example_supabase)。

---

## 摘要

本指南探讨了如何使用一体化数据管理器 **Brick**、作为远程后端的 **Supabase** 以及用于本地缓存的 **SQLite**，来构建健壮的离线优先 Flutter 应用程序。通过在本地存储和远程服务器之间保持数据的一致性，Brick 确保了您的移动应用无论在何种网络连接状态下，都能保持完全的功能性与响应能力。

> This guide explores how to build robust, offline-first Flutter applications using **Brick**—an all-in-one data manager—combined with **Supabase** as a remote backend and **SQLite** for local caching. By maintaining data parity between local storage and remote servers, Brick ensures your mobile app remains fully functional and responsive regardless of network connectivity.

---

## 为什么要选择离线优先？

应用最糟糕的版本永远是无法使用的那个版本。用户经常处于低连接率的环境中，例如地铁、飞机或 3G 以下的网络。采用离线优先架构设计，能够保证在无法保证稳定带宽时提供无缝的用户体验。

> The worst version of your app is always the unusable one. Users frequently navigate low-connectivity environments such as subways, airplanes, or sub-3G connections. Designing for an offline-first architecture guarantees a seamless user experience when steady bandwidth cannot be guaranteed.

即使对于纯在线应用，Brick 也能显著减少往返延迟（RTT），因为从 Supabase 获取的所有数据都会存储在本地缓存中。后续查询会立即检索本地副本，从而降低延迟和网络成本。此外，如果 SQLite 的性能尚不能满足需求，Brick 还提供了一个内存缓存层。在离线状态下进行的任何请求都会自动放入队列中，并不断重试，直到恢复网络连接，从而确保本地状态与远程状态保持完美同步。

> Even for online-only applications, Brick dramatically reduces round-trip times because all data fetched from Supabase is stored in a local cache. Subsequent queries retrieve the local copy instantly, lowering latency and network costs. Furthermore, if SQLite performance isn't sufficient, Brick offers an in-memory cache layer. Any requests made while offline are automatically placed in a queue and continually retried until network connectivity is restored, ensuring your local and remote states stay perfectly synchronized.

对于敏感数据或必须保持最新状态的数据，您还可以轻松地在每个请求的基础上[选择不使用缓存](https://getdutchie.github.io/brick/#/offline_first/policies)。

> For sensitive or must-be-fresh data, you can easily [opt-out of the cache](https://getdutchie.github.io/brick/#/offline_first/policies) on a request-by-request basis.

---

## 快速上手

### 1. 创建 Flutter 应用
```bash
flutter create my_app
```

> ```bash
> flutter create my_app
> ```

### 2. 添加依赖
将所需的 Brick 依赖项添加到您的 `pubspec.yaml` 中：

> Add the required Brick dependencies to your `pubspec.yaml`:

```yaml
dependencies:
  brick_offline_first_with_supabase: ^1.0.0
  sqflite: ^2.3.0
  brick_sqlite: ^3.1.0
  uuid: ^3.0.4

dev_dependencies:
  brick_offline_first_with_supabase_build: ^1.0.0
  build_runner: ^2.4.0
```

### 3. 设置目录
为 Brick 生成的序列化和数据库文件创建必要的目录：

> Create the necessary directories for Brick's generated serialization and database files:

```bash
mkdir -p lib/brick/adapters lib/brick/db
```

### 4. 定义模型
Brick 通过代码生成技术桥接了远程数据和本地存储。创建一个模型定义文件，将您的 Dart 字段映射到 Supabase 表的列：

> Brick bridges remote data and local storage via code generation. Create a model definition file that maps your Dart fields to your Supabase table columns:

```dart
// Your model definition can live anywhere in lib/**/* as long as it has the .model.dart suffix
// Assume this file is saved at my_app/lib/src/users/user.model.dart

import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
import 'package:brick_supabase/brick_supabase.dart';
import 'package:uuid/uuid.dart';

@ConnectOfflineFirstWithSupabase(
  supabaseConfig: SupabaseSerializable(tableName: 'users'),
)
class User extends OfflineFirstWithSupabaseModel {
  final String name;

  // Be sure to specify an index that **is not** auto-incremented in your table.
  // An offline-first strategy requires distributed clients to create
  // indexes without fear of collision.
  @Supabase(unique: true)
  @Sqlite(index: true, unique: true)
  final String id;

  User({
    String? id,
    required this.name,
  }) : this.id = id ?? const Uuid().v4();
}
```

### 5. 生成代码
一旦定义好模型，便可运行 build_runner：

> Once your models are defined, run the build runner:

```dart
dart run build_runner build
```

该命令将生成用于与 Supabase 进行序列化/反序列化的适配器，以及针对任何新增、删除或修改的列的 SQLite 迁移脚本。

> This command generates adapters for serialization/deserialization with Supabase, along with SQLite migration scripts for any new, dropped, or modified columns. 

> ⚠️ **注意：** 每次修改模型后，请重新运行此命令以确保适配器能够正确地进行序列化和反序列化。

> > ⚠️ **Note:** After every model modification, re-run this command to ensure your adapters serialize and deserialize correctly.

---

## 存储库 (Repository)

您的应用逻辑不需要直接与 SQLite 或 Supabase 交互。通过单一的 Repository 入口进行交互，Brick 在底层处理了缓存和获取的复杂性，同时为在线和离线状态提供了统一的 API。

> Your application logic doesn't need to interact with SQLite or Supabase directly. By interacting through a single repository entrypoint, Brick handles the complexity of caching and fetching under the hood while providing a consistent API for both online and offline states.

### 配置 Repository

> ### Configuring the Repository

```dart
// Saved in my_app/lib/src/brick/repository.dart
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
// This hide is for Brick's @Supabase annotation; in most cases,
// supabase_flutter **will not** be imported in application code.
import 'package:brick_supabase/brick_supabase.dart' hide Supabase;
import 'package:sqflite_common/sqlite_api.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import 'brick.g.dart';

class Repository extends OfflineFirstWithSupabaseRepository {
  static late Repository? _instance;

  Repository._({
    required super.supabaseProvider,
    required super.sqliteProvider,
    required super.migrations,
    required super.offlineRequestQueue,
    super.memoryCacheProvider,
  });

  factory Repository() => _instance!;

  static Future<void> configure(DatabaseFactory databaseFactory) async {
    final (client, queue) = OfflineFirstWithSupabaseRepository.clientQueue(
      databaseFactory: databaseFactory,
    );

    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseAnonKey,
      httpClient: client,
    );

    final provider = SupabaseProvider(
      Supabase.instance.client,
      modelDictionary: supabaseModelDictionary,
    );

    _instance = Repository._(
      supabaseProvider: provider,
      sqliteProvider: SqliteProvider(
        'my_repository.sqlite',
        databaseFactory: databaseFactory,
        modelDictionary: sqliteModelDictionary,
      ),
      migrations: migrations,
      offlineRequestQueue: queue,
      // Specify class types that should be cached in memory
      memoryCacheProvider: MemoryCacheProvider(),
    );
  }
}
```

### 在 `main()` 中初始化

> ### Initializing in `main()`

```dart
import 'package:my_app/brick/repository.dart';
import 'package:sqflite/sqflite.dart' show databaseFactory;

Future<void> main() async {
  await Repository.configure(databaseFactory);
  // .initialize() does not need to be invoked within main().
  // It can be invoked from within a state manager or an initState()
  await Repository().initialize();
  runApp(MyApp());
}
```

> 💡 **平台说明：** 所选的 `databaseFactory` 取决于您的平台。对于单元测试，请使用 `import 'package:sqflite_common_ffi/sqflite_ffi.dart' show databaseFactory`。有关在 [web](https://github.com/tekartik/sqflite/tree/master/packages_web/sqflite_common_ffi_web#use-the-proper-factory)、[Linux](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#linux) 或 [Windows](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#windows) 上的具体安装说明，请参考 SQFlite 文档。

> > 💡 **Platform Note:** The chosen `databaseFactory` depends on your platform. For unit tests, use `import 'package:sqflite_common_ffi/sqflite_ffi.dart' show databaseFactory`. Refer to SQFlite's documentation for specific installation instructions on [web](https://github.com/tekartik/sqflite/tree/master/packages_web/sqflite_common_ffi_web#use-the-proper-factory), [Linux](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#linux), or [Windows](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#windows).

---

## 使用方法

Brick 的 DSL 查询编写一次，即可同时转换为本地和远程集成。

> Brick's DSL queries are written once and translated for both local and remote integration.

### 基本查询
检索所有名为 "Thomas" 的用户：

> ### Basic Queries
> To retrieve all users named "Thomas":

```dart
await Repository().get<User>(query: Query.where('name', 'Thomas'));
```

### 关联查询
通过模型关联进行查询：

> ### Association Queries
> To query by model associations:

```dart
// Assuming we had a model `Order` with a `user` association
await Repository().get<Order>(query: Query.where('user', Where.exact('name', 'Thomas')));
```

高级查询可以利用诸如 `contains`、`not`、`like` 以及子句等操作符（不过请注意，并非所有 Supabase 操作符都开箱即用）。

> Advanced queries can leverage operators like `contains`, `not`, `like`, and sub-clauses (though note that not all Supabase operators are supported out-of-the-box).

### 响应式 (Reactivity)
您可以从应用程序的任何地方订阅更新后的本地数据流。例如，执行下拉刷新将更新本地存储，并自动通知所有活动的流监听器：

> ### Reactivity
> You can subscribe to a stream of updated local data from anywhere in your application. For instance, performing a pull-to-refresh will update local storage and notify all active stream listeners automatically:

```dart
final Stream<List<User>> usersStream = Repository().subscribe<User>(query: Query.where('name', 'Thomas'));
```
*注意：默认情况下不使用 Supabase 通道，尽管支持选择加入的实时功能目前正在积极开发中。*

> *Note: This does not use Supabase channels by default, though opt-in real-time features are currently under active development.*

### 写入/更新数据 (Upserting Data)
创建的模型可以直接上传到 Supabase，而无需手写 JSON 序列化：

> ### Upserting Data
> Created models can be uploaded directly to Supabase without manual JSON serialization:

```dart
await Repository().upsert<User>(User(name: 'Thomas'));
```
所有关联的模型都将被[自动写入 (upserted)](https://getdutchie.github.io/brick/#/supabase/models?id=upsert-behavior)。

> All attached associations will be [upserted automatically](https://getdutchie.github.io/brick/#/supabase/models?id=upsert-behavior).

---

## 其他小贴士

### 外键与关联
您可以轻松地连接相关的模型和数据库表：

> ### Foreign Keys and Associations
> You can effortlessly connect related models and database tables:

```dart
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
import 'package:brick_supabase/brick_supabase.dart';
import 'package:my_app/lib/src/users/user.model.dart';
import 'package:uuid/uuid.dart';

@ConnectOfflineFirstWithSupabase(
  supabaseConfig: SupabaseSerializable(tableName: 'orders'),
)
class Order extends OfflineFirstWithSupabaseModel {
  // Specifying a foreignKey is optional and only necessary if there are
  // multiple joins pointing to the same table.
  // @Supabase(foreignKey: 'user_id')
  final User user;

  @Supabase(unique: true)
  @Sqlite(index: true, unique: true)
  final String id;

  Order({
    String? id,
    required this.user,
  }) : this.id = id ?? const Uuid().v4();
}
```

### 单元测试
快速模拟您的 Supabase 端点以编写清晰的单元测试：

> ### Unit Testing
> Quickly mock your Supabase endpoints to write clean unit tests:

```dart
import 'package:brick_supabase/testing.dart';
import 'package:test/test.dart';

void main() {
  final mock = SupabaseMockServer(modelDictionary: supabaseModelDictionary);

  group('MyClass', () {
    setUp(mock.setUp);
    tearDown(mock.tearDown);

    test('#myMethod', () async {
      final req = SupabaseRequest<MyModel>();
      final resp = SupabaseResponse([
        await mock.serialize(MyModel(name: 'Demo 1', id: '1')),
        await mock.serialize(MyModel(name: 'Demo 2', id: '2')),
      ]);

      mock.handle({req: resp});
      final provider = SupabaseProvider(mock.client, modelDictionary: supabaseModelDictionary);
      final retrieved = await provider.get<MyModel>();
      expect(retrieved, hasLength(2));
    });
  });
}
```

---

## 延伸阅读

Brick 在底层管理了大量事务，这有时可能会让人感到不知所措。然而，它已经在成千上万台设备上支撑了五年多的生产级应用，为 Flutter 开发提供了一种经过实战检验的架构。

> Brick manages a great deal under the hood, which can occasionally feel overwhelming. However, having powered production apps across thousands of devices for over five years, it provides a battle-tested architecture for Flutter development.

* **示例项目：** [Brick 与 Supabase 结合](https://github.com/GetDutchie/brick/tree/main/example_supabase)
* **视频：** [Brick 架构](https://www.youtube.com/watch?v=2noLcro9iIw)（包含[补充的披萨类比](https://medium.com/flutter-community/brick-your-app-five-compelling-reasons-and-a-pizza-analogy-to-make-your-data-accessible-8d802e1e526e)）
* **视频：** [Brick 基础](https://www.youtube.com/watch?v=jm5i7e_BQq0)（核心机制概述）
* **官方指南：** [使用 Flutter 和 Supabase 构建用户管理应用](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)

> * **Example Project:** [Brick with Supabase](https://github.com/GetDutchie/brick/tree/main/example_supabase)
> * **Video:** [Brick Architecture](https://www.youtube.com/watch?v=2noLcro9iIw) (includes a [supplemental pizza analogy](https://medium.com/flutter-community/brick-your-app-five-compelling-reasons-and-a-pizza-analogy-to-make-your-data-accessible-8d802e1e526e))
> * **Video:** [Brick Basics](https://www.youtube.com/watch?v=jm5i7e_BQq0) (an overview of core mechanics)
> * **Official Guide:** [Build a User Management App with Flutter and Supabase](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)