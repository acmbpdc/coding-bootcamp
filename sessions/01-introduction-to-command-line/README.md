# Introduction to Command Line

A command line interface (CLI) is a means of interacting with a computer system where the user (or client) issues commands to the system in the form of successive lines of text (command lines).

---

## Motivation 

Although they may seem archaic, command line interfaces are extremely practical :

*   Almost all major organizations use *powerful remote systems* that are 100 times faster than your average personal computer.

    These remote systems almost never use a Graphical User Interface and can be operated solely via commands.

*   With the rise of Cloud Computing, Big Data, Deep Learning and Blockchain, the *command line workflow has proven to be the best*.

*   Apart from its demand in the industry, command line expertise brings with it a *holistic idea about the operating system*.

*   Command line also provides *greater control over a system* and various methods to *automate boring tasks*.

Using the command line interface is very similar to solving a puzzle. With the right approach, anything is possible.

---

## Environment

Over the course of this workshop, we will work in a Linux environment.

The workspaces are mounted on a Telnet server, at `172.16.22.5`

To connect to it:

*   Open a terminal and run the following command if you are on a macOS, Linux or other Unix based system:

    ```bash
    telnet 172.16.22.5
    ```

*   If you are on a Windows system :
    *   Ensure that the Telnet service is enabled by navigating to `Control Panel` > `Programs and Features` > `Turn Windows features on or off` > Check `Telnet Client`
    *   Hit `Windows` + `R` and enter the following command :
    
    ```powershell
    telnet 172.16.22.5
    ```

If you have followed the instructions, you would have successfully connected to the telnet server. Enter your credentials to access your workspace.

Once successfully authenticated, you should see the following prompt :

```
[username@linuxbpdc1 ~]$
```

---

## Basics

Use the `echo` command to print stuff

```bash
echo "Hello, world."
```

```bash
echo 'Single quotes also work'
```

---

Write single line comments with `#`

```bash
# Anything to the right of the # is ignored by the command line interface
```

---

Use the `man` command to describe commands

```bash
man echo # This gives a manual about "echo" . Press 'q' to exit
```

---

## Navigation

When working with a GUI, we navigate across the filesystem using a file explorer :

*   File Explorer (Windows)
*   Finder (macOS)

The `pwd` command tells you the present working directory

```bash
pwd # If you ever got lost,`pwd` will tell you exactly where you are
```
​
You are currently in your `HOME` directory which is the equivalent of `Desktop` on PCs.

---

All files and directories on a computer system have a unique path that describes their location :

*   An **absolute path** refers to the same location in a file system relative to the *root directory*
*   A **relative path** points to a specific location in a file system relative to the *present working directory*

Some important shorthand notations : 

*   `.` refers to the pwd
*   `..` refers to the parent of pwd
*   `/` refers to the root directory

---

The `cd` command changes the pwd to a specified path

```bash
cd .. # Changes pwd to its parent. You can confirm this using "pwd"
```

---

We can look at the contents of a directory using `ls`

```bash
ls
```

You should be seeing all the `HOME` directories of students in your year

---

You can format this output using flags

```bash
ls -l # formatted as a list
```

```bash
ls -al # displays all files (including hidden ones) in a list format
```

---

You can chain `..` switch to a directory that is an ancestor of the pwd

```bash
cd ../../.. # in this case , it takes you to the root directory
```

To return to your `HOME` directory, run *ONE* of the following :

*   ```bash
    cd # not specifying a path teleports you back home
    ```

*   ```bash
    cd $HOME # The $HOME variable stores the absolute path of your HOME directory
    ```

*   ```bash
    cd ~ # ~ = $HOME
    ```

Jump back to root and try all the above ways

```bash
cd / # jumps back to root, since "/" is the absolute path for root
```

---

## Files

Once you are back in your home directory, create a folder

```bash
mkdir foldername
```