#include <iostream>
#include <string>

//主要功能：这是一个简单的C++程序，演示了如何使用输入输出流、字符串和循环结构。程序输出一个问候语，并展示了一个简单的循环。
int main() {
    std::string name = "World";
    std::cout << "Hello, " << name << "!" << std::endl;

    // Simple demonstration of a loop and a function call
    for (int i = 1; i <= 3; ++i) {
        std::cout << "Iteration " << i << std::endl;
    }

    return 0;
}
