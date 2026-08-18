---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 人工智能
- 博弈论
- 强化学习
- 策略优化
- 决策支持系统
title: CoupVisor：基于回合与质疑决策支持的策略优化
---
### 文章背景与核心概要
本文介绍了 **CoupVisor**，这是一个专为隐信息卡牌游戏《政变》（Coup）设计的高级决策支持系统。该系统旨在解决游戏中的两大核心问题：玩家在每个回合应该采取什么行动，以及何时应该质疑对手的声明。通过将游戏事件标准化并结合角色概率与手牌数量，CoupVisor 能够精准评估声明的真实性，同时避免在无证据的开局阶段产生误判。

研究通过广泛的模拟实验表明，基于获胜导向（Win-oriented）的奖励系统在性能上显著优于传统的启发式基线和短期奖励方法。该框架打通了手动对局、对局回放、模拟、信念追踪以及机器学习策略，为复杂隐信息博弈中的策略优化提供了重要的技术参考。

---

## Summary

> **CoupVisor** is an advanced decision-support system designed for the hidden-information card game *Coup*. It assists players by determining optimal actions for each turn and deciding when to challenge an opponent's claims. 
> 
> The framework standardizes game events across manual play, replays, simulations, belief tracking, and machine learning policies. By combining role likelihoods with the number of cards held by a claimant, CoupVisor accurately estimates the truthfulness of a claim—correctly avoiding false suspicions on opening moves. Through extensive simulation, the research demonstrates that employing a win-oriented reward system significantly outperforms heuristic baselines and short-term reward approaches.

---

## Paper Metadata

* **arXiv Identifier:** [arXiv:2608.15868](https://arxiv.org/abs/2608.15868)
* **Subjects:** Artificial Intelligence (`cs.AI`); Computer Science and Game Theory (`cs.GT`); Machine Learning (`cs.LG`)
* **Author:** Cris Huynh
* **Submitted On:** August 16, 2026
* **Comments:** 15 Pages and 9 pages of appendix

---

## Abstract

> This paper presents CoupVisor, a decision-support system for the hidden-information card game Coup. It addresses two questions: what a player should do on each turn, and when a player should challenge an opponent's claim. The system is built around a single description of game events, which is shared across manual play, replay of recorded games, simulation, belief tracking, advisor recommendations, and learning-based policies. CoupVisor estimates the chance that a claim is truthful by combining how likely each role is with how many cards the claimant still holds, which corrects a case where the very first claim of a game was flagged as suspicious despite no evidence. We compare a rule-following advisor and several learned and heuristic players across many simulated games and different opponent styles. Our main finding is that the choice of reward, whether it rewards short-term gains or ultimately winning the game, decides which learning approach performs best, and that a win-oriented reward produces a policy that outperforms all baselines.

---

## Full-Text & Resources

* [View PDF](https://arxiv.org/pdf/2608.15868)
* [HTML Version (Experimental)](https://arxiv.org/html/2608.15868v1)
* [TeX Source](https://arxiv.org/src/2608.15868)
* [License](http://creativecommons.org/licenses/by/4.0/) 
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>