title: 自学指南 Flex & Bison
Date: 2016-10-12 09:33

因为公司在用 phalcon，这种 c 扩展的框架 IDE 没有办法补全，所以想写一个把 zephir 转译成 PHP IDE Helper 的东西。本来想直接 Reflection 取一下类信息就好了，奈何最终效果不理想，本来 [Zephir](https://zephir-lang.com/) 中有的很多信息都丢掉了，注释也全部没有。所以还是要用 passer 转译。  

只能说兴趣果然是最好的老师。之前编译原理看三段打瞌睡，死活读不下去，这下却是兴致满满了。只是Flex、Bison入门资料太少，网上写的那些文章都是浅尝辄止，完全没有可实践性。读手册又太过乏味。

看来看去，还是[动物书的 Flex & Bison](http://web.iitd.ac.in/~sumeet/flex__bison.pdf) 读起来舒服。

对于词法分析语法分析完全没有概念的同学，可以先看看[这个 PDF](http://www.capsl.udel.edu/courses/cpeg421/2012/slides/Tutorial-Flex_Bison.pdf) 了解一下，再读动物书会好一些，不然有些没头没脑。内容基本和书里的第一章重合，但简单介绍了一下 Flex/Bison 是用来做什么的。

总结：
1. [这个 PDF](http://www.capsl.udel.edu/courses/cpeg421/2012/slides/Tutorial-Flex_Bison.pdf) 
2. [动物书的 Flex & Bison](http://web.iitd.ac.in/~sumeet/flex__bison.pdf)
