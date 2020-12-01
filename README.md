# loops

![alt text][logo]

Examples of looping constructs in a bunch of languages - just in case, you know, you were asking for a friend. As indeed, a friend was.

## Looping by language ...

Here, we focus on the languages are either themselves interesting, or used by people who have a sense of humour. The criteria for this initial list was established by including languages which are known to have been used to implement the [Rockstar language](https://github.com/RockstarLang/rockstar). Why? Because coding in song lyrics is as amusing as it is pointless, and  my friend can't include [Fetlang](https://github.com/fetlang/fetlang). If you want a worthy and extensive list of programming languages, then you can check that out [elsewhere](https://en.wikipedia.org/wiki/List_of_programming_languages).

### C

The Violent Femmes said to ["Add it Up"](https://www.youtube.com/watch?v=QHapDS2fcFE), so [here goes](https://www.w3resource.com/c-programming/c-for-loop.php)

```
#include<stdio.h>
main()
{
int sum; int x; sum=0;
 for(x=1;x<=50;++x) 
 // x take values in {1,2,3,...,50}
 {
 sum = sum + x; 
 }
 printf(" 1+2+...+50=%d\n",sum);
}
```

### Go

So, let's start mapping out the basiscs: ["a" is for apple](https://gobyexample.com/range) ...

```
kvs := map[string]string{"a": "apple", "b": "banana"}
for k, v := range kvs {
  fmt.Printf("%s -> %s\n", k, v)
}
```

### Haskell

Don't [take recursion](http://learnyouahaskell.com/recursion) lying down - it's your lot for looping.

```
take' :: (Num i, Ord i) => i -> [a] -> [a]  
take' n _  
    | n <= 0   = []  
take' _ []     = []  
take' n (x:xs) = x : take' (n-1) xs  
```


### Java

The best ever entry in the obfuscated C contest was an entry that [looked like Java](https://www.ioccc.org/2005/chia/chia.c). In [this example](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html) will [Len](https://en.wikipedia.org/wiki/Len_Goodman) give them a 9, 10, or a [spinal-tap-ish](https://www.youtube.com/watch?v=KOO5S4vxi0o) 11?

```
class ForDemo {
    public static void main(String[] args){
         for(int i=1; i<11; i++){
              System.out.println("Count is: " + i);
         }
    }
}
```

### Javascript

Don't get caught out [deep in the caverns](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)

```
for (let step = 0; step < 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log('Walking east one step');
}
```
### Kotlin

The Duke of York marched the army up the hill, [and down again](https://kotlinlang.org/docs/reference/control-flow.html)

```
for (i in 1..3) {
    println(i)
}
for (i in 6 downTo 0 step 2) {
    println(i)
}
```


### OCaml

Are we going to float away, or is this the end, [period](https://ocaml.org/learn/tutorials/if_statements_loops_and_recursion.html)?

```
let string_of_float f =
  let s = format_float "%.12g" f in
  let l = string_length s in
  let rec loop i =
    if i >= l then s ^ "."
    else if s.[i] = '.' || s.[i] = 'e' then s
    else loop (i+1) in
  loop 0
```

### Python

There's more than one way to loop in this Swiss-Army knife of a language. But focusing on breakfast reminds me I am hungry ...

```
def eat(item):
	print("yum, I had %s"%item)

menu = ["bacon","eggs","tattie scone","black pudding", "beans", "coffee"]

for item in menu:	
    eat(item)
```

### Ruby

It's a [gem](https://ruby-doc.org/docs/ruby-doc-bundle/Tutorial/part_02/loops.html), time to leave the launchpad.

```
count = 10
10.times do
    count -= 1
	puts count
end
puts "Lift off!"
```

### Rockstar

Any language with poetic number literal system is going to take some extra time to parse mentally, but at least you sing it while you wait (https://codewithrockstar.com/docs). Here's a loop - but does it run 16, or 17 times?

```
Tommy was a dancer
While Tommy ain't nothing,
Knock Tommy down
```

### Rust

If at first you don't succeed, you could try again a few times, [maybe](https://doc.rust-lang.org/rust-by-example/flow_control/loop.html). 

```
fn main() {
    let mut count = 0u32;

    println!("Let's count until infinity!");

    // Infinite loop
    loop {
        count += 1;

        if count == 3 {
            println!("three");

            // Skip the rest of this iteration
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, that's enough");

            // Exit this loop
            break;
        }
    }
}
	
```

## NSFW

Stuff that you might want to cut out before sharing in your own materials. 

### Fetlang

Fetlang is intended to look like poorly-written fetish erotica, so you'll probably be too busy blushing (or thinking WTF?) to comprehend the actual code. Comments in this [example](https://esolangs.org/wiki/Fetlang) are in paranthesis. It's all adding up in this example.

```
(Set Sean to an empty chain)
Make Sean moan

(Set Carrie to 0(a fraction))
Worship Carrie's feet
 
(Have Amy cycle through a chain listing arguments given, separated by '\0'(a fraction))
Bind Amy to Saint Andrew's Cross

    (Add Amy(a fraction) to Sean)
    Have Amy hogtie Sean

    (If Amy is '\0', print out the current argument, and reset Sean)
    If Amy is Carrie's bitch
        Make Slave scream Sean's name
        Make Sean moan
```

## Contributing

Didn't see some a language you were expecting? Got a better line of comedy to offer? Please feel free to offer interesting examples, especially where they make me laugh, and/or differ in language or structure from existing examples. To contribute, please fork, and make a pull request. Include your example in alphabetical order, or in the NSFW section if it is well, not safe for work (or school). Obfuscated, arcane, and otherwise programmatically-problematic examples are also welcome - so long as they are interesting. There is no implied quality in the examples below. For your example to be accepted, the original source needs to be acknowledged/linked,  and it must be from open-source code which you can include in an MIT-licensed repo. Please include a brief explanation in the text why your example is interesting, or even better, provide some kind of obscure hint about what it is doing, so that this page is at least a tiny bit amusing. This is not a reference work that is meant to be useful.


[logo]: ./img/logo.png "looping spiral with arrow"
