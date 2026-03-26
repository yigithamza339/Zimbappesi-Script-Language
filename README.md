# Zimbappesi-Script-Language
Zimbappesi is Mini Script Language and IDE

# Zimbappesi Programming Language 🚀

**Zimbappesi** is a lightweight, specialized programming language characterized by its unique memory management and structured syntax. It operates using its own core library, **scu** (Standard Code Utils), and follows a specific execution flow.

> [!NOTE]
> Zimbappesi is currently in its early development stage. The features below represent the core syntax of the current build.

---

## 🖥 Editor Features

You can manage your code files easily through the **File** menu at the top of the interface:
* **Save:** Use the **Save** option to save the code you have written.
* **Open:** Use the **Open** option to load and view your previously saved code files.

---

## 🛠 Core Components & Syntax

* **Standard Library (scu):** The language relies on the `scu` (Standard Code Utils) library for fundamental operations.
* **Memory Management:** Code execution begins within `int buffer.main`, defining the memory space for the program.
* **Strict Punctuation:** Every command and comment **must** terminate with a semicolon (`;`).
* **Variable Declaration:** Data types like integers are stored using specific `.Value` wrappers and curly braces `{ }`.

---

## 💻 Code Example

Here is a look at the basic syntax and how to write a simple program:

```Zimbappesi
// Calling the Standard Code Utils library and placing it into a .Child value ;
Namespace = scu.Child; 

// Initializing the memory area and opening the code block ;
int buffer.main(int main*) {   

    // Printing a string to the console ;
    print.console.write.String{"Hello World!"};  

    // Saving an integer value (requires curly braces, no quotes) ;
    int.Value{years = 9}; 

    // Printing a saved variable to the console using .Var ;
    print.console.write.Var{years}; 

    // Performing arithmetic operations (supports +, -, *, /) ;
    print.console.write.Var{years * 9}; 

// Closing the code block ;
}
