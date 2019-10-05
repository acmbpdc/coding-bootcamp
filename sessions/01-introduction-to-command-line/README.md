# Introduction to Command Line

<!-- Please refer to this if you haven't https://github.com/jlevy/the-art-of-command-line?utm_campaign=explore-email&utm_medium=email&utm_source=newsletter&utm_term=daily -->
A command line interface (CLI) is a means of interacting with a computer system where the user (or client) issues commands to the system in the form of successive lines of text (command lines).

---

## Motivation 

Although they may seem archaic, command line interfaces are extremely practical:

*   Almost all major organizations use *powerful remote systems* that are 100 times faster than your average personal computer.

    These remote systems almost never use a Graphical User Interface and can be operated solely via commands.

*   With the rise of Cloud Computing, Big Data, Deep Learning and Blockchain, the *command line workflow has proven to be the best*.

*   Apart from its demand in the industry, command line expertise brings with it a *holistic idea about the operating system*.

*   Command line also provides *fine-grained control over a system* and various methods to *automate boring tasks*.

Using the command line interface is very similar to solving a puzzle. With the right approach, anything is possible. You just need to know the right commands from a large toolbox.

---

## Environment

Over the course of this workshop, we will work in a Linux environment.
<!-- Explain Linux in brief. Link to Linux foundation/FOSS/FSF please -->
<!-- Ellaborate that what will be taught in the following would be partially or completely inapplicable in windows shells. CMD and Powershell. https://github.com/PowerShell/PowerShell/blob/master/docs/learning-powershell/README.md -->

The workspaces are mounted on a Telnet server, at `172.16.22.5`
<!-- Friend please kindly let them know that the server is sitting right behind them -->
<!-- At least mention that communications over telnet are in plaintext -->

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

If you have followed the above instructions, you would have successfully connected to the telnet server. Enter your credentials to access your workspace.
<!-- Stress that they are accessing a linux system from within a windows computer/Mac OS -->

Once successfully authenticated, you should see the following prompt :

```
[username@linuxbpdc1 ~]$
```
<!-- WHAT IS THIS DOLLAR FRIENDS??? -->
---

## Basics

Use the `echo` command to print stuff <!-- Contrast with printf maybe? -->

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
<!-- do not confuse with password: passwd -->

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
<!-- Mention that ls means list/listing -->

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

Jump back to root and try all the above options.
<!-- https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi_xb_i3oXlAhWQFxQKHUKnBksQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.linux.com%2Ftutorials%2Flinux-filesystem-explained%2F&psig=AOvVaw18D7px0J7nfdIDlqqM5Bay&ust=1570386239637429 -->

```bash
cd / # jumps back to root, since "/" is the absolute path for root
```

---

## Files

Once you are back home, create a directory

```bash
mkdir dirname # creates a directory named 'dirname' in the pwd
```

Move into this new directory

```bash
cd dirname
```

Now, create a file

```bash
touch myfile.txt # creates a file named 'myfile.txt'
```
<!-- Please explain finger command and other kinky commands friend -->

You can use `ls` command to look at the details of this file
<!-- Quiz: which command can detail the contents of the file -->

A little about files:

*   _All_ files contain data. <!-- Quiz: What about empty files? -->
*   Files are stored in the computer's _secondary memory_
*   The file's data is stored in the form of _bytes_

For text files:

*   The bytes that represent this data take values in a _particular range_.
*   This range is determined by the _encoding_ used, which may be [ASCII](https://en.wikipedia.org/wiki/ASCII), [UTF-8](https://en.wikipedia.org/wiki/UTF-8) etc.
*   When being rendered, _specific characters_ that match the bytes of these files are shown.
*   Sometimes there are bytes that do not make sense so they don't get rendered properly.

Most systems have in-built text editors. Let us use the `nano` editor <!-- why not vim or emacs? -->

```bash
nano myfile.txt # opens 'myfile.txt' with nano
```

Type something in.

The text that is shown are not the exact contents of the file. 
This data is held by the `nano` editor as a buffer and is residing in the RAM of the system.
To save the contents of the file :

*   Hit `Ctrl` + `X` to write the contents of the buffer into the file
*   Hit `Y` to confirm and `Enter`
*   Nano now shows the name of the file it is about to write into. You can change this if you like. Hit `Enter` to finish.

Use the `cat` command to display the contents of the file

```bash
cat myfile.txt
```

Use the `head` command to display the first few lines of the file

```bash
head myfile.txt # head prints the first 10 lines by default
```

You can change the number of lines by providing a flag

```bash
head myfile.txt -n 5 # prints the first 5 lines
```

Similarly, you can display the last few lines with `tail`

```bash
tail myfile.txt -n 8 # prints the last 8 lines of the file
```

Create files with the following content :

```
# billy.txt
Billy is a cat
```

```
# tommy.txt
Tommy is a dog
```

To avoid a messy workspace it is a good idea to organize your files.

Create a directory for 'cats' and 'dogs'

You should have the following files and directories
```
billy.txt  cats  dogs  myfile.txt  tommy.txt
```

We can move files into specific directories.

Try one of the following commands to move 'billy.txt' into 'cats' :

*   ```bash
    mv billy.txt cats/ # billy.txt is moved into the directory 'cats'
    ```
*   ```bash
    mv billy.txt cats/billy.txt # renames billy.txt as 'cats/billy.txt' and hence moves it into 'cats'
    ```

Similarly, move 'tommy.txt' into 'dogs'

Be very careful when using the `mv` command :

When `/` is not specified at the end of the name of a directory, it renames the source to the destination instead of moving it inside.

```bash
mv billy.txt cats # renames billy.txt to cats.
```

In this case the the 'cats' <!-- watch for peeps confusing with cat command --> directory is unchanged but 'billy.txt' is renamed to 'cats'

To better visualize the contents of `pwd` use the `tree` command

```bash
tree # displays the names of files and directories in the pwd in a recursive manner
```

We can create copies of files using the `cp` command :

```bash
cp myfile.txt yourfile.txt # makes a copy of 'myfile.txt' and calls it 'yourfile.txt'
```

Copy 'billy.txt' and 'tommy.txt' into `pwd`

```bash
cp cats/billy.txt ./
cp dogs/tommy.txt ./
```

We can scale these operations to affect multiple files 

```bash
mkdir textfiles
mv *.txt textfiles/ # This moves all files that have '.txt' as their extension into the directory 'textfiles'
```

## Permissions

Everything on a system has permissions attached with it.
Since files, directories & programs all have permissions of their own, there is a very elaborate permission mechanism.

View the details of the contents in the `pwd`

```bash
ls -al
```

You should see the following characters next to each entity in the directory

```
drwxr-xr-x
```

These characters represent the permissions for a particular entity :

*   The first character describes the type of entity
    *   ***d*** for **directory**
    *   ***c*** for **charcater** special file
    *   ***-*** for a **regular** file
*   The next 9 characters are in fact 3 groups of characters that represent permissions for different users
    *   The *first 3* show the permissions for the **owner** of the file
    *   The *second 3* show the permissions for the **group** associated with that file
    *   The *last 3* show the permissions for the **rest** of the users
*   Each group of 3 characters represents the 3 major permissions
    *   ***r*** for **read** and is equivalent to *4*
    *   ***w*** for **write** and is equivalent to *2*
    *   ***x*** for **execute** and is equivalent to *1*

A permission of *5* allows only *read* and *execute* (4 + 1 = 5).

File permissions can be changed by :

*   The owner
*   `root` i.e. any superuser

Use the `chmod` command to change permissions

```bash
chmod 777 cats # allows anyone (owner, group and rest) to do anything (read, write and execute) to 'cats'
```

The `chown` command can be used to change the ownership of a file but can only be called by `root`

## Miscellaneous


Use the `wc` command to count display :

*   The number of lines
*   The number of words
*   The number of characters

```bash
wc myfile.txt
```

You can use flags to limit the output to what you need

```bash
wc myfile.txt -l # shows the number of lines for 'myfile.txt'
```

Use the `grep` command to search for specific characters in a file

```bash
grep "cat" myfile.txt # shows the lines which have 'cat'
```

An import feature of the Bash shell is the pipe system. 
It enables the output of one command to be used as the input for another.
We can combine the two commands

```bash
grep "cat" myfile.txt | wc -l # shows the number of lines that have the word 'cat'
```

The `history` command shows your command history

```bash
history
```

Try to search for a particular command in your history

```
history | grep "cd"
```

<!-- Lastlog maybe? -->

## Summary
