---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-11-10
hide:
- navigation
tags:
- AI智能体
- 基础设施
- KV缓存
- 推理成本
title: Agentic AI 将在撞上智能之墙前先撞上基础设施之墙
---
# Agentic AI 将在撞上智能之墙前先撞上基础设施之墙

*模型能力的进化速度，远远超过了我们承载其实际运行需求的基础设施能力。*

> *The Models Are Improving Faster Than Our Ability to Serve What They’re Being Asked to Do.*

<img alt="" class="attachment- size- wp-post-image webpexpress-processed" decoding="async" fetchpriority="high" height="941" sizes="(max-width: 1672px) 100vw, 1672px" src="./images/d63e502bbbbf.png" width="1672"/>

### 文章背景与核心概要
当前行业关于 AI 智能体 (AI Agent) 的争论大多聚焦于模型能否可靠规划、自主纠错等算法“智商”层面，但真正决定智能体能否走出实验室、迈向万级规模化落地的，却是底层的工程基础设施与单机经济账。与单轮“即问即答”的传统对话模型不同，AI 智能体在漫长的多轮工具调用与外部接口等待期间，必须让昂贵的 GPU 显存全程驻留巨大的键值缓存 (KV Cache)；即便显卡在等待期毫无计算负载，显存也无法释放，直接导致单机并发容量断崖式暴跌。再叠加串行工具调用带来的累加延迟以及层层放大的隐性重试风暴，大规模运行智能体的服务成本将迅速攀升到不可承受的天价。要想跨越这堵高耸的“基础设施之墙”，不能坐等基座模型自我进化，而必须通过并发工具调用、将会话时长纳为核心容量指标，以及实现显存换入换出与分页缓存等务实工程突破来重塑基础设施。

---

## 核心内容摘要

> ## Summary

关于 AI 智能体未来走向的讨论，大多聚焦在模型本身的智能与能力上限——比如它能否可靠地制定计划、能否在犯错后自我纠错、能否做出靠谱的自主决策。然而，真正决定智能体能否实现规模化落地的致命瓶颈，其实是底层基础设施与单机经济账 (Unit Economics)。与“一问一答、用完即走”的简单对话聊天机器人不同，AI 智能体必须维护一个漫长而活跃的会话；在此期间，即便利存等待外部工具或第三方 API 响应而毫无计算负载，也必须持续霸占昂贵的 GPU 显存来保存键值缓存 (KV Cache)。这种显存锁定，再加上串行执行带来的累加延迟以及层层放大的隐性重试循环，在规模化部署时会引发不可承受的服务成本。要想攻克这堵“基础设施之墙”，不能指望只等前沿基座模型变得更聪明，而是需要依靠务实的工程手段，例如工具并发执行、精细化会话生命周期管理以及优化上下文缓存架构。

> While the debate around Agentic AI often centers on intelligence and capability—such as planning, error recovery, and autonomous decision-making—the true bottleneck to scaled deployment is infrastructure and unit economics. Unlike simple conversational chatbots, AI agents maintain active sessions that consume high-value GPU memory (KV cache) even while waiting on external tool calls or APIs. Combined with sequential execution bottlenecks and compounding retry loops, this creates an unsustainable serving cost at scale. Overcoming this "infrastructure wall" requires practical engineering solutions, such as concurrent tool execution, intelligent session duration management, and optimized context caching, rather than relying solely on frontier model improvements.

---

目前关于 AI 智能体发展方向的大多数探讨，几乎都在围绕“模型能力”打转：大模型究竟能否制定出周密的计划？执行受挫时能否自我纠错？涉及关键后果的真实行动，我们敢不敢放手交给它去操作？

> Most of the argument about where AI agents are headed is an argument about capability. Can the model plan reliably? Can it recover from its own mistakes? Can it be trusted with an action that has consequences?

这些确实是亟待攻克的真问题。但它们并不是决定未来几年智能体能否实现大规模落地的决定性因素。因为有一道更加迫近、到来速度更快的硬约束正在逼近：在推理服务架构中，承载智能体运行的单机经济效益极为尴尬；更棘手的是，大家梦寐以求想要赋予智能体的种种强大能力，反而在以同等幅度加剧这种尴尬。

> Those are real questions. They’re also not the ones that will decide whether agents get deployed at scale over the next few years, because there’s a nearer constraint and it’s arriving faster. Agents are economically awkward to serve, and the awkwardness grows with exactly the capabilities everyone wants to add.

---

## 聊天机器人与智能体属于截然不同的计算负载

> ## A Chatbot and an Agent Are Different Workloads

传统的对话式请求本质上是一次性的单程往返。用户输入提示词，大模型吐出 Token，连接随即关闭。作为系统架构师，你可以对多请求进行批量处理 (Batching)，可以复用公共前缀缓存，并且用一个简单的吞吐量数字就能算清系统的服务容量。

> A conversational request is one round trip. Prompt in, tokens out, connection closed. You can batch it, cache the prefix, and reason about throughput with a single number.

但智能体请求却是一个复杂的持续会话 (Session)。它往往需要发起工具调用，然后原地等待；读取返回的结果后，再思考下一步动作，接着调用下一个工具，历经数轮周折之后才最终给出答案。即便是完成一项中等难度的任务，通常也需要反复调用六到八次大模型，而两次调用之间往往穿插着漫长的等待。

> An agent request is a session. It calls a tool, waits, reads the result, decides what to do next, calls another tool, and eventually answers. A modest task might be six or eight model invocations with waiting in between.

两者之间的根本差异与模型“聪不聪明”毫无关系，却深刻影响着工程实现。在各个步骤交替的间隙，智能体必须持续维持上下文状态——包括历史对话记录、各个工具的返回结果以及逐步累积的推理过程。在服务后端，这些会话状态全部以 [KV 缓存 (KV Cache)](https://arxiv.org/abs/2309.06180) 的形式驻留在昂贵的 GPU 显存中；只要会话尚未结束，这部分显存就必须全程被其霸占，哪怕智能体在此期间花费了数秒钟仅仅是在傻傻等待某个外部第三方 API 的响应。

> That difference matters for a reason that has nothing to do with intelligence. Between steps, the agent is holding state — the conversation, the tool outputs, the accumulated reasoning. On the serving side that state lives in GPU memory as [KV cache](https://arxiv.org/abs/2309.06180), and it occupies memory for the entire duration of the session, including the seconds the agent spends waiting on an API that isn’t you.

因此，衡量推理系统承载能力的度量单位，不再是传统的“每秒请求数 (Requests Per Second, RPS)”，而是变成了“显存常驻并发会话数”。在同一套硬件配置上，一套原先可以游刃有余地支撑每秒上千次常规对话请求的推理系统，在面对智能体会话时，可能仅仅并发几十个会话就会将显存彻底吃饱瘫痪。

> So the unit of capacity stops being “requests per second” and becomes “concurrent sessions resident in memory.” A system that comfortably served a thousand conversational requests per second may serve a few dozen concurrent agent sessions on the same hardware.

---

## 漫长的等待，才是最昂贵的成本开销

> ## The Waiting Is the Expensive Part

这里暴露出了一个令人极其难受的工程特性：在发起外部工具调用的过程中，智能体本身其实处于静止状态。此时既没有生成任何 Token，也没有消耗任何算力。然而，GPU 显存却依然被死死占用着——因为如果将这段上下文从显存中驱逐出去、等响应回来后再重新计算一遍，其代价甚至比一直霸占显存还要高昂。

> Here’s the uncomfortable property. During a tool call, the agent is doing nothing. No tokens are being generated. No compute is being consumed. The GPU memory, however, is still occupied, because evicting and recomputing that context would cost more than holding it.

这就导致了极其荒谬的资源浪费：你机房里最昂贵顶级的 GPU 算力硬件，在很多时刻竟然只是在为一次正在等待数据库返回查询结果的请求干坐着“占座”。

> Your most expensive hardware is reserved for a request that is, at that moment, waiting on a database query.

在传统的分布式系统中，这类问题早在很多年前就已经有了标准解法：工作线程在发起 IO 请求后立刻释放硬件资源，待外部响应抵达后再恢复现场继续执行。但在大模型推理场景下，要做到这一点就意味着必须将庞大的 KV 缓存从 GPU 显存换出 (Evict) 到主机内存或本地固态硬盘，并在需要时再换入恢复；而这一数据搬运过程的数据传输开销极为惊人，以至于绝大多数现行系统根本不敢轻易尝试。[针对这一难题的学术与工程研究](https://arxiv.org/abs/2303.06865) 目前异常活跃，而它之所以备受瞩目，恰恰是因为这个问题在商业上的代价太高了。

> In conventional distributed systems we solved this a long time ago — you release the resource and pick the work back up when the response arrives. Doing the same for model serving means evicting KV cache to host memory or disk and restoring it, and the transfer cost is high enough that most systems don’t bother. [Research on exactly this](https://arxiv.org/abs/2303.06865) is active, and it’s active because the problem is expensive.

---

## 串行执行让问题雪上加霜

> ## Sequential Execution Makes It Worse Than It Needs to Be

目前市面上几乎所有的智能体框架，在执行工具调用时都是按部就班地一条接一条串行推进。大模型先请求查询天气，等待结果返回；接着请求检查日程日历，等待返回；然后再请求搜索航班动态，继续等待返回。

> Nearly every agent framework executes tool calls one after another. The model asks for a weather lookup, gets it, asks for a calendar check, gets it, asks for a flight search, gets it.

但在很多情况下，这三项查询调用之间根本没有任何依赖关系，它们完全可以同时并行触发。如果采取串行执行，整个请求的端到端延迟就是所有调用耗时的简单相加；而如果改为并发执行，总延迟就直接缩减为耗时最长的那一个调用。

> Frequently those three calls have no dependency on each other. They could have run at the same time. Executed sequentially, the latency is the sum. Executed concurrently, it’s the longest one.

这并不是什么仅针对智能体的全新洞见——任何需要在既定延迟预算内调度多个微服务或多模型的系统，都遵循这一基础架构规律：总延迟应当取决于任务依赖图上的最长关键路径，而不是所有步骤的盲目累加。然而，这一规律在智能体场景下之所以显得尤为致命，是因为智能体会话在整个生命周期内都牢牢霸占着 GPU 显存。因此，压缩真实物理时间 (Wall-Clock Time) 不仅能显著改善终端用户的交互体验，更会直接提升单台硬件能够并发容纳的会话数量。

> This isn’t a novel observation about agents — it’s the same structural point that applies to any system running multiple models or services inside one latency budget. Total latency should be the longest path through the dependency graph, not the sum of every stage. The reason it matters more for agents is that the session is resident in GPU memory for the whole duration, so cutting wall-clock time doesn’t just improve the user’s experience, it directly increases how many sessions fit on the hardware.

只要将单次会话的持续时长缩短一半，在完全不更换 GPU 硬件、不对模型做任何改动的前提下，集群的并发承载能力就能直接翻倍。

> Halve session duration and you roughly double concurrent capacity, on the same GPUs, with no model change.

---

## 悄然放大的重试风暴：无人设计的级联灾难

> ## Retries Compound in a Way Nobody Designed

现代智能体框架通常会直接沿用底层 HTTP 网络库的默认重试策略，最常见的默认值便是自动重试三次。

> Agent frameworks inherit retry defaults from the HTTP libraries underneath them. Usually three attempts.

与此同时，大模型本身也会以它特有的方式发起重试。当某个工具返回了不符合预期的无用结果时，具备推理能力的模型往往会自主调整策略，换另一种方式重新尝试——这在本质上同样是一次重试，只不过它是由模型自主推理触发、从未被任何人显式配置过。

> The model also retries, in its own way. When a tool returns something unhelpful, a reasoning model will often try a different approach — which is a retry, just one that nobody configured.

当这两层机制叠乘在一起时，灾难就诞生了：外层被固化了三次网络重试策略，而内层模型又自主思考出三种替代方案并依次重试，最终演变成了一场高达九次的级联重试，而这一切甚至未曾在任何架构设计文档中体现。更致命的是，每一次重试都是一次完整的大模型前向推理调用，需要重新生成大量 Token 并消耗实打实的 GPU 运行时间。

> Stack those and a three-attempt policy wrapped around a model that independently reasons its way into three more approaches is a nine-attempt policy that no one wrote down. Each of those attempts is a full model invocation, with its own tokens and its own GPU seconds.

当底层依赖的某个服务出现性能劣化变慢时，这种隐性放大效应便会将局部的性能抖动直接推向系统性瘫痪；更可怕的是，大模型单次重试所耗费的计算成本，相比于传统 REST 接口重试高出了数个数量级。

> When a dependency slows down, this amplification is what turns degradation into an outage, and it does so at a cost per attempt that’s orders of magnitude above a retried REST call.

---

## “基础设施之墙”的真实模样

> ## What the Wall Actually Looks Like

这堵阻碍智能体落地的硬墙，并不是什么高深莫测的模型能力天花板，而是一个极其现实、甚至有些枯燥的单机经济账问题。正是它，将无数雄心勃勃的 AI 创新项目死死拦截在从“概念验证 (PoC)”走向“生产上线”的关键分水岭之前。

> Not a capability ceiling. Something more mundane: a unit-economics problem that stops projects at the pilot-to-production boundary.

在小规模试点测试阶段，一切看似运转良好：面向十来个内部用户，响应延迟尚可接受，账单金额微不足道。但当业务团队尝试将其推演至一万名并发用户时，测算出的 GPU 显卡采购需求瞬间变成了一个天文数字——这并不是因为模型本身的推理速度太慢，而是因为每一个并发会话在其整个生命周期中都死死咬住显存不放，而这个生命周期的大部分时间，实际上全都在毫无意义地等待。

> The pilot works. It’s ten users, latency is acceptable, and the bill is a rounding error. Then someone models it at ten thousand users and the GPU requirement is implausible — not because the model is slow, but because concurrent sessions each hold memory for their full lifetime, and lifetime includes waiting.

正是在这个测算阶段，无数原本前景广阔、令人兴奋的企业内部原型 Demo，不得不悄无声息地下线夭折。

> This is the stage at which a lot of promising internal demos quietly stop.

---

## 如何打破这堵基础设施之墙？

> ## What Moves the Wall

破局的方法并不神秘玄乎，而且所有的突破口全部集中在底层基础设施的工程改造上，而非等待模型算法本身的突破：

> Nothing exotic, and all of it is infrastructure rather than modelling:

* **并发执行无依赖的独立工具调用**：这是当前无需采购任何新硬件即可立刻兑现的最大性能红利。
* **将会话持续时长确立为核心容量度量指标**：不要再单纯盯着每秒 Token 生成数或 GPU 利用率。真正关键的是状态在显存中的常驻时间有多长，以及当前显存究竟能容纳多少个并发会话。
* **在系统全局统筹重试预算，而非按单次调用孤立设置**：引入全局重试预算上限（例如将重试流量严格限制在总流量的较小比例以内），彻底遏制前文所述的级联指数放大。Google SRE 在[过载处理 (Handling Overload)](https://sre.google/sre-book/handling-overload/) 中的经典工程实践，以及 Envoy 的[重试预算 (Retry Budgets)](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter) 机制，都早已在传统微服务体系中验证了这一思路。
* **将逻辑推理与具体执行解耦分离**：调用高参数量的顶尖大模型负责制定高阶规划，而将机械繁琐的中间执行步骤交由轻量级的小模型完成。智能体日常处理的大多数常规操作，根本不需要劳烦前沿基座模型。
* **大幅降低上下文显存换出与恢复的成本**：积极引入量化 KV 缓存、[分页注意力 (PagedAttention)](https://docs.vllm.ai/en/latest/) 机制，并为处于空闲等待状态的会话开辟低成本换出通道。这正是当下大模型推理服务工程领域最具创新价值的前沿阵地。

> *   **Execute independent tool calls concurrently:** The largest single win, available today, requiring no new hardware.
> *   **Treat session duration as the capacity metric:** Not tokens per second. Not GPU utilization. How long state stays resident, and how many sessions fit.
> *   **Budget retries across the system rather than per call:** A global cap — retries as a small percentage of total traffic — prevents the compounding described above. Google’s SRE practice on [handling overload](https://sre.google/sre-book/handling-overload/) and Envoy’s [retry budgets](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter) both implement this idea outside the AI stack.
> *   **Separate reasoning from execution:** A large model to plan, a much smaller one for the mechanical steps. Most of what an agent does doesn’t need a frontier model.
> *   **Make context eviction cheap:** Quantized KV cache, [paged attention](https://docs.vllm.ai/en/latest/), and offload paths for idle sessions. This is where the most interesting serving work is happening right now.

---

基座模型的能力必定会持续演进，这一点毋庸置疑。但 AI 智能体最终究竟能够成长为支撑千行百业的底层基础设施，还是沦为停留在实验室里的昙花一现的 Demo，取决于那些看似并不起眼、缺乏光环的工程底座——我们究竟能否高效承载这种“一边漫长等待外部响应、一边持续占用昂贵显存”的全新计算负载；我们能否彻底摆脱为串行调用的机械累加买单，转而只为关键路径上的最大耗时付费。

> The models will keep improving. That part looks reliable. Whether agents become infrastructure or stay demos depends on something less glamorous — whether we can serve a workload that holds expensive memory while it waits, and whether we stop paying the sum of a sequence when we could be paying its longest path.

*针对上述最后一点——即在单一延迟预算内并发执行具备依赖关系的模型调用，作者在论文 [《机器学习系统中模型路由的异步推理图执行》 (Asynchronous Inference Graph Execution for Model Routing in Machine Learning Systems)](https://doi.org/10.14445/22312803/IJCTT-V72I10P101) (发表于《国际计算机趋势与技术期刊》72(10)，2024年10月) 中提出了底层的执行模型。关于将生成式模型深度整合至受严格延迟约束的决策系统的更多实践，可参阅 [《大模型增强型交易与决策平台：弥合生成式智能与金融决策系统》 (LLM-Augmented Trading and Decision Platforms: Bridging Generative Intelligence with Financial Decision Systems)](https://doi.org/10.5281/zenodo.18223142) (发表于《信息系统工程与管理期刊》11(1s)，2026年)。*

> *I published the execution model underlying that last point — concurrent execution of dependent model calls within a single latency budget — in [“Asynchronous Inference Graph Execution for Model Routing in Machine Learning Systems”](https://doi.org/10.14445/22312803/IJCTT-V72I10P101), International Journal of Computer Trends and Technology 72(10), October 2024. On the integration of generative models into latency-bound decision systems specifically, see [“LLM-Augmented Trading and Decision Platforms: Bridging Generative Intelligence with Financial Decision Systems”](https://doi.org/10.5281/zenodo.18223142), Journal of Information Systems Engineering and Management 11(1s), 2026.*

---

### 关于作者

> ### About the Author

**Gangadharan Venkataraman** 长期致力于实时机器学习与智能决策平台的系统架构设计。他拥有佐治亚理工学院 (Georgia Institute of Technology) 计算机科学硕士学位，并在超大规模分布式系统和工业级生产环境机器学习基础设施领域拥有十余年的深入实践经验。

> **Gangadharan Venkataraman** works on architecture for real-time machine learning and decision platforms. He holds an M.S. in Computer Science from the Georgia Institute of Technology and has spent over a decade building large-scale distributed systems and production ML infrastructure.

* [jedify.com](https://jedify.com/)
* [LinkedIn 个人主页 (LinkedIn Profile)](https://www.linkedin.com/in/ganga5v/)

> * [jedify.com](https://jedify.com/)
> * [LinkedIn Profile](https://www.linkedin.com/in/ganga5v/)
