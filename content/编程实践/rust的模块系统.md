Title: Rust 模块系统初探
Tags: Rust,模块

学习一门编程语言，知道如何引用外部的文件或者说模块系统是比较重要的一点，PHP用`autoload`机制，C有经典的`include`。最近写 [wslexe](https://github.com/jswh/wslexe) 的时候，因为原作者用的 rust，所以就简单学习了一下。但是 rust 的模块文档是从顶部设计开始写的，很多概念，有些复杂，这里写一个应用导向的学习笔记。

##### 引入文件

首先，让我们初始化一个项目。

```shell
mkdir rustmod
cd rustmod
cargo init
```

我们得到了下面这样的基础项目结构

```shell
rustmod
├── Cargo.toml
└── src
    └── main.rs
```

`main.rs`里面只有一个简单的输出的‘hello world’的`main`函数。我们新增一个`functions.rs`文件，将生成字符串的过程做成一个函数，供`main`函数调用。

```rust
//file: rustmod/src/functions.rs
pub fn hello(name: String) -> String {
    format!("Hello, {}!", name)
}
```

`functions.rs`就成为了一个单文件模块，rust 中称为`mod`，模块的名称就是文件的名称。模块内部的函数，只能在模块内部使用，如果要在模块外调用，需要用`pub`关键词，显式声明函数可在外部使用，我自己把这个叫导出函数。

下面我尝试在`main`函数中使用`functions`模块。使用的方式很简单，只要在使用前声明一下模块就可以了。声明模块使用`mod`关键字。使用模块内函数的时候，需要用`::`进行调用。

```rust
mod functions;//声明模块
fn main() {
    let s = functions::hello("World".to_string());
    println!("{}", s)
}
```

如果去掉函数前的`pub`关键词，编译器就会报错。

```shell
error[E0603]: function `hello` is private
```

##### 模块的嵌套

rust 除了一个文件作为一个模块之外，还持支模块的嵌套。嵌套的方式，有两种。

第一种是在一个文件内，用`mod`关键字定义子模块。比如，我修改`functions.rs`

```rust
//file: rustmod/src/functions.rs
pub mod util {
    pub fn hello(name: String) -> String {
        format!("Hello, {}!", name)
    }
}
```

同样，模块也是私有的，要在外部调用也需要`pub`关键字修饰。对应的`main`函数就要改为

```rust
//file: rustmod/src/main.rs
mod functions;
fn main() {
    let s = functions::util::hello("World".to_string());
    println!("{}", s)
}
```

第二种形式，是用文件夹来组织模块。文件夹的名字是模块的名字，rust 会去寻找文件夹下面的`mod.rs`作为模块的主文件，可以在里面写任意的 rust 代码，不过大多数时候用来输出目录内的子模块。我们来新建一个`util`文件夹，作为一个工具库的模块，修改项目结构

```shell
rustmod
├── Cargo.toml
└── src
    ├── main.rs
    └── util
        ├── functions.rs
        └── mod.rs
```

在`mod.rs`输出`functions`模块。同样也需要用`pub`关键词修饰，否则就只是`mod.rs`文件内的私有子模块。

```rust
//file: rustmod/src/util/mod.rs
pub mod functions;
```

修改`main.rs`中的调用

```rust
//file: rustmod/src/main.rs
mod util;
fn main() {
    let s = util::functions::util::hello("World".to_string());
    println!("{}", s)
}
```

##### 总结

rust 的模块由`mod`关键字和文件系统两者结合定义。`mod`关键字用来声明一个模块的名字，模块的内容或直接以`mod NAME {MOD CONTENT}`的形式书写，或根据严格的规则查找对应源文件。文件查找规则有以下几点：

1. 查询声明模块的文件所在目录中对应模块名称名字的`NAME.rs`文件，如果有就作为模块使用。
2. 查询声明模块的文件所在目录中对应模块名字`NAME`的文件夹，并且文件夹内有`mod.rs`文件，如果有就以`mod.rs`文件作为模块使用。
3. 上面的规则都可以互相嵌套。

我尝试了在`src`目录下，同时存在`util.rs`和`util`文件夹，编译的时候报错

```shell
error[E0584]: file for module `util` found at both util.rs and util/mod.rs
```

所以还有第四条规则：

4. 在同一层级不能同时存在文件夹和文件类型的模块，否则会名字冲突。

