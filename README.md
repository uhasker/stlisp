# stlisp

A **s**uper **t**iny **Lisp** (in Python).
Obvious inspiration is [obvious](https://norvig.com/lispy.html).
Yes, this is a gimmick.

## Starting the REPL

Clone the repository and start the REPL with `python3 stlisp.py`.

## Language features

### Numbers

Numbers:

```
stlisp> 2
2
stlisp> 0.5
0.5
```

### Symbols

Defining symbols with `define`:

```
stlisp> ('define', 'x', 2)
None
stlisp> 'x'
2
```

### Arithmetic

Arithmetic:

```
stlisp> ('neg', 4)
-4
stlisp> ('add', 2, 4)
6
stlisp> ('sub', 2, 4)
-2
stlisp> ('mul', 2, 4)
8
stlisp> ('truediv', 2, 4)
0.5
stlisp> ('pow', 2, 4)
16
stlisp> ('abs', -4)
4
stlisp> ('mod', 2, 4)
2
stlisp> ('floordiv', 2, 4)
0
stlisp> ('round', 2.75, 1)
2.8
```

### Comparison

Comparison:

```
stlisp> ('eq', 2, 4)
False
stlisp> ('ne', 2, 4)
True
stlisp> ('le', 2, 4)
True
stlisp> ('lt', 2, 4)
True
stlisp> ('ge', 2, 4)
False
stlisp> ('gt', 2, 4)
False
```

### Working with lists

Building lists with `cons`:

```
stlisp> ('cons', 1, 2)
(1, 2)
stlisp> ('cons', 1, ('cons', 2, 3))
(1, 2, 3)
stlist> ('cons', 1, ('cons', 2, ('cons', 3, 4)))
(1, 2, 3, 4)
```

Using `car` and `cdr`:

```
stlisp> ('car', 'lst')
1
stlisp> ('cdr', 'lst')
(2, 3, 4)
```

Procedures useful for working with lists:

```
stlisp> ('define', 'lst', ('cons', 1, ('cons', 2, ('cons', 3, 4))))
None
stlisp> ('len', 'lst')
4
stlisp> ('sum', 'lst')
10
stlisp> ('min', 'lst')
1
stlisp> ('max', 'lst')
4
```

### Defining procedures

Define procedures with `define` and `lambda`:

```
stlisp> ('define', 'double', ('lambda', ('x',), ('mul', 'x', 2)))
None
stlisp> ('double', 16)
32
```

### Closures

Stlisp has closures:

```
stlisp> ('define', 'x', 2)
None
stlisp> ('define', 'addX', ('lambda', ('y',), ('add', 'x', 'y')))
None
stlisp> ('addX', 5)
7
```

Closures can be arbitrarily nested:

```
stlisp> ('define', 'x', 2)
None
stlisp> ('define', 'y', 4)
None
stlisp> ('define', 'addXY', ('lambda', (), ('lambda', (), ('add', 'x', 'y'))))
None
stlisp> ('addXY', ())
<function stlisp_eval.<locals>.<lambda> at 0x7f185cbc8430>
stlisp> (('addXY', ()), ())
6
```

You can set variables in outer environments using `set!`:

```
stlisp> ('define', 'x', 10)
stlisp> ('define', 'incX', ('lambda', (), ('set!', 'x', ('add', 'x', 1))))
None
stlisp> ('x')
11
```

### Conditionals

Stlisp has conditionals:

```
stlisp> ('if', ('eq', 4, 4), 2, 3)
2
```

### Using quote

Stlisp has `quote`:

```
stlisp> ('quote', (1, 2, 3))
(1, 2, 3)
stlisp> ('quote', 'x')
x
stlisp> ('len', ('quote', 'hello'))
5
```
