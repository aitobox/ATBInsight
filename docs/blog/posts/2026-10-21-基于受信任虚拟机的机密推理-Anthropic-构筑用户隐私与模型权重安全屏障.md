---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-10-21
hide:
  - navigation
tags:
  - Anthropic
  - 机密计算
  - 机密推理
  - 模型权重安全
  - 隐私保护
title: "基于受信任虚拟机的机密推理：Anthropic 构筑用户隐私与模型权重安全屏障"
---

# 基于受信任虚拟机的机密推理：Anthropic 构筑用户隐私与模型权重安全屏障

> # Confidential Inference via Trusted Virtual Machines

### 文章背景与核心概要
数以百万计的用户每天向大语言模型 (Large Language Model, LLM) 交付私有代码、商业战略等高敏感数据，如何在享受顶尖 AI 生产力的同时实现绝对的数据保密，已成为 AI 产业亟待攻克的信任基石。为此，Anthropic 携手 Pattern Labs 展开前沿安全研究，正式公布了名为“机密推理 (Confidential Inference)”的技术框架。该方案依托基于硬件隔离的受信任虚拟机 (Trusted Virtual Machine) 与密码学度量机制，构建起端到端的强信任链，确保敏感数据——无论是用户输入的提示词还是前沿模型自身的核心权重，除在受到硬件密码学隔离与代码签名远程验证的极小执行区瞬时解密外，在其余所有传输与存储链路中始终保持全密文形态。这项突破性探索不仅从根本上化解了云端隐私外泄的隐忧，更为主权级模型资产保护树立了全新的技术标杆。

---

## 摘要

> ## Summary

Anthropic 正在积极研发**机密推理 (Confidential Inference)** 技术，这是一套旨在通过密码学手段为用户数据隐私和模型权重安全提供绝对保障的核心工具集。在与 Pattern Labs 的合作研发中，该项目确保了各类敏感数据（如用户提交的提示词和模型核心专有权重）在整个系统生命周期内全程处于高强度加密状态，仅在受限、可验证且由硬件物理隔离的专属环境中进行实际计算时才被短暂解密。

> Anthropic is researching and developing **Confidential Inference**, a set of tools designed to provide cryptographic guarantees for user data privacy and model weight security. Published in collaboration with Pattern Labs, this initiative ensures that sensitive data (such as user prompts and proprietary model weights) remains encrypted everywhere except inside restricted, verifiable, and hardware-isolated environments during active processing.

---

## 前言

> ## Introduction

每天有数以百万计的用户将高度敏感的信息交付给 Claude，涵盖专有核心代码、商业战略规划乃至机密企业情报。为了将这种基于人际合同的信任升华为密码学级别的确定性保障，Anthropic 正全力研发**机密推理 (Confidential Inference)** 框架——该架构能够确保加密数据只在那些具备密码学自证能力的受信任服务器内部被解密与计算。

> Millions of users entrust Claude with sensitive information, ranging from proprietary code to confidential business strategies. Anthropic is researching ways to make this trust cryptographically guaranteed through **Confidential Inference**—a framework that processes encrypted data only within servers that can prove themselves trustworthy.

引入这套机密计算工具主要服务于两大核心目标：

1. **模型权重安全 (Model Weight Security)**：全面保护 Claude 等前沿模型的核心资产，抵御高级持续性威胁 (APT) 攻击者的窃取；
2. **用户数据安全 (User Security)**：在密码学层面严格证实用户的敏感数据享有绝对隐私，不受任何第三方及云端宿主的窥探。

> Adopting these tools serves two primary purposes:
> 1. **Model Weight Security:** Securing frontier models like Claude against advanced threat actors.
> 2. **User Security:** Proving that sensitive user data remains private.

*阅读完整学术白皮书：[机密推理技术论文 (Confidential Inference Paper)](https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf)*。

> *Read the full [Confidential Inference Paper](https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf).*

---

## 推理服务体系架构

> ## Inference Service

机密推理的核心准则在于：所有敏感数据除在实际发生计算的瞬时点外，必须在任何环节均处于加密状态。为了落地这一铁律，Anthropic 融合了前沿的机密计算 (Confidential Computing) 理念，在系统内部构建起牢不可破的信任链 (Chain of Trust)。

> The core principle of Confidential Inference is that sensitive data must remain encrypted except at the exact point of processing. To enforce this, Anthropic uses confidential computing principles to build a chain of trust.

对于用户输入的数据，全系统仅在以下两个阶段短暂接触明文 (Cleartext)：

* **API 服务器 (The API Server)**：接收原始提示词，将其编码转换为 Token，并执行处理 Claude API 请求所必需的控制流逻辑。
* **推理服务器 (The Inference Server)**：在专用硬件加速器上运行 Claude 的核心神经网络“大脑”，进而自回归生成最终的补全 Token。（*对于专有模型权重而言，仅有推理服务器有权触碰这些关键敏感资产*）。

> For user data, cleartext (unencrypted text) handling occurs at two points:
> * **The API Server:** Handles prompts, transforms them into tokens, and operates logic behind Claude API requests.
> * **The Inference Server:** Runs the "brains" of Claude on hardware accelerators to generate completion tokens. *(For model weights, only the Inference Server receives sensitive data).*

鉴于目前市面上绝大部分底层硬件加速器尚未完全原生普及机密计算特性，Anthropic 另辟蹊径，在受信任执行环境中部署了一个小巧而坚固的**“模型加载与调用器 (Model Loader and Invoker)”**来作为安全桥梁。

> To work around hardware accelerators that do not yet fully support confidential computing, Anthropic is exploring a small, secure **"model loader and invoker"** running within a trusted environment.

### 加载器的工作机制

> ### How the Loader Works:

* 负责接收加密形态的模型与输入数据，在受保护内存中完成安全解密，随后送入加速器；
* 发起对底层硬件加速器的计算调用，并将加速器输出的原始结果重新加密打包后返回；
* 在虚拟化监控器 (Hypervisor) 的严格硬件隔离下充当“虚拟加速器”，并且仅接受经由高安全持续集成 (CI) 服务器签名核验的合法受控代码。

> * Accepts encrypted data, decrypts it, and sends it to the accelerator.
> * Invokes calls against the accelerator and returns encrypted results.
> * Acts as a "virtual accelerator" isolated by a hypervisor, accepting only code signed via secure continuous integration servers.

---

## 受信任执行环境

> ## Trusted Environment

该安全加载器运行在一个高标准的机密计算环境之中，具备以下核心安全特性：

1. **硬件加密内存**：通过硬件芯片级物理隔离，杜绝外部宿主及其他同机工作负载的窥探；
2. **强制关闭调试功能**：在硬件与固件层面禁用 JTAG、GDB 内存挂钩等一切侵入式调试接口；
3. **密码学完整性证明**：提供严密的密码学度量证据，证实当前正在执行的代码正是经过严格安全审计的既定版本。

> The secure loader operates inside a confidential computing environment featuring:
> 1. **Encrypted memory**, isolated by hardware from other workloads.
> 2. **Disabled debugging features**.
> 3. **Cryptographic proof** that the correct, reviewed code is being executed.

系统利用受信任平台模块 (Trusted Platform Module, TPM) 对服务器系统的每个启动引导阶段进行逐层哈希度量，生成一份用于证明该服务器环境完整可靠的密码学证明。独立的密钥管理服务器 (Keyserver) 在收到请求后会严密核验该证明，**唯有**当请求方毫无瑕疵地证明自身绝对安全时，才会下发解密密钥。

> A Trusted Platform Module (TPM) measures each boot stage and generates a hash attesting to the server's integrity. A keyserver evaluates this proof and releases decryption keys *only* when the recipient proves it is secure.

---

## 未来演进方向

> ## Future Directions

伴随前沿大模型的持续演化升级，未来还可以在安全加载器层集成更为严密的防御措施，包括：

* 对持有明文模型权重的服务器施加严格的出网流量带宽限制 (Egress Bandwidth Limitations)，从物理链路上杜绝海量模型权重的外泄可能；
* 在正式执行推理前，强制要求通过前置安全分类器的数字签名背书。

> As frontier models advance, additional safeguards may be integrated at the secure loader layer, including:
> * Egress bandwidth limitations on servers holding cleartext model weights.
> * Requiring signatures from safety classifiers before running inference.

---

## 总结与结论

> ## Conclusions

采用这一套机密推理架构，为用户的每一次交互请求赋予了完整可靠的安全生命周期保障：

1. 用户请求在离开客户端、抵达 Anthropic 云端服务器之前已全量加密；
2. API 服务器在受保护隔离区解密、执行预处理逻辑后，再度以加密形态打包转发；
3. 推理服务器接收到的是完全加密的请求载荷，唯有在内部受信任加载器中才会进行极短暂的解密运算；
4. 预测补全结果在离开安全加载器之前便已重新加密，并以密文形式原路返回给调用者。

> Using this Confidential Inference model ensures a secure lifecycle for user requests:
> 1. Requests are encrypted before arriving at Anthropic servers.
> 2. The API server decrypts, processes, and re-encrypts the request.
> 3. The Inference Server handles the request in encrypted form, decrypting it solely within the trusted loader.
> 4. Completions are encrypted before leaving the loader and returned to the caller.

模型权重的安全生命周期则更为纯粹高效：在静态存储和网络传输时全程加密，仅在受信任加载器内短暂解密加载至加速核心，任何未经授权的明文形态都绝不可能流出边界之外。

> Model weights follow a simpler lifecycle: they are stored encrypted, decrypted strictly at the loader, and never released externally.

Anthropic 呼吁各芯片硬件厂商在未来的计算芯片中原生集成更为完善的机密计算技术，共同缩小信任边界，筑牢下一代 AI 算力底座。

> Hardware designers are encouraged to integrate native confidential computing into their chips to further reduce the trust boundary.

* **查阅完整技术报告：** [机密推理技术论文 (Confidential Inference Paper)](https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf)

> * **Read the full report:** [Confidential Inference Paper](https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf)

---

### 加入我们

> ### Work With Us

如果你对这项前沿安全研究充满热情并渴望参与其中，欢迎前往 [Anthropic 招聘主页 (Anthropic Jobs Page)](https://www.anthropic.com/jobs) 投递“安全 (Security)”以及“AI 研究与工程 (AI Research and Engineering)”相关的在招岗位。

> If this research inspires you, consider applying for open roles in the "Security" and "AI Research and Engineering" sections on the [Anthropic Jobs Page](https://www.anthropic.com/jobs).
