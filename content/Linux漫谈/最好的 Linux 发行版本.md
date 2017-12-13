title: 最好的 Linux 发行版  
Date: 2017-12-10 11:24  
Category: Linux 漫谈
Tags: Linux, WSL, Winsows, Subsystem
标题是个玩笑话。

Linux 作为一个操作系统，在服务器领域尤其是web服务器来说，一直是一个不错的选择，甚至在市场份额上，还略微高于 Windows Server。但在桌面端，似乎一直是 geek 的玩物，哪怕是 web 开发，有钱的直接上 MacOS，没钱的想方设法组黑苹果。除了驱动不完善之外（现在情况已经大大改善了），最主要的还是 Linux 的桌面端应用相比其他两个操作系统生态来说，还是太少太少。一些仅有的软件，对比之下质量也只是勉强可用的地步。

但是，作为一个web开发者，不熟悉 Linux 系统，可以说是一个重大的技能缺陷。因为不论你怎么躲，都躲不开 Linux 系统的使用。哪怕你用的的 .Net，难道你就不看看 .Net core 了嘛。诚然，我们日常使用中并不会使用到太多的功能。即使常见如看日志，实在不行就拉到本地来看嘛。但如果会用head、tail、less、grep，那基本的查询分分钟搞定，再如果会用sed、awk，简单的日志统计也是不在话下。

对 Linux 常用的命令和工具有基本的了解，知道什么情况下可以用什么，是每个有志向的 web 开发者的基本能力。

但是（凡事都有个但是），作为日常操作系统，linux 是真难用。特别是中国这种特殊国情，没有QQ，没有微信，基本就丧失了日常使用的可能。不要说web版、wine版，那都是没有办法的办法。也难怪，web 开发们都用 mac。甚至从某种角度讲，MacOS 是 Linux 的替代品，虽然有些不同，但同出于 *nix 门下的 MacOS，相比 Windows 还是更接近生产环境一些，各种工具链也基本一致。

直到微软在 Build 2016 大会，宣布了 Bash on Windows。正式的名称是Windows Subsystem for Linux，简称 WSL。简单来说，Windows 的 NT 内核在设计之初就可以支持多种子系统，只要封装 NT 的系统调用为对应系统的 API 即可为应用系统提供支持。具体原理可以参看[Windows Subsystem for Linux Overview](https://blogs.msdn.microsoft.com/wsl/2016/04/22/windows-subsystem-for-linux-overview/)。英文不好的话，[知乎](https://zhuanlan.zhihu.com/p/21856725)上有对应的中文翻译。

经过一年的开发与完善，在今年的秋季更新中，WSL 结束测试，进入应用商店, Bash on windows这个名称也不再使用。windows10 就这样成为了“最好的 Linux 发行版”。

对如果开发工作设计Linux的底层，特别是驱动级别的开发，以及 Linux 下单 UI 开发还是需要虚拟系统，或者最好是原生系统，这方面不太了解，也不班门弄斧了。但就 Linux 的入门学习和一般的服务器端开发工作来说, WSL已经完全可以胜任。虽然与开发工具的集成上上还有一些问题（大多数的开发工具还不支持调用 WSL 里的工具链, VsCode 已经在做[相关工作](https://github.com/Microsoft/vscode/labels/WSL)），但问题不大。对于web开发来说，编译运行这些工作这些使用命令行处理也不繁琐，个人也更喜欢使用命令行。而 vim 和 emacs 用户，则几乎不存在什么问题了。

我最近切换到了 window10 与 WSL 的组合，经过最初几天的适应，现在已经非常顺手。就开发而言，基本没有什么不同了。至于如何启用WSL，网上有太多文章了。[这里](https://winaero.com/blog/enable-wsl-windows-10-fall-creators-update/)是微软的官方教程。
