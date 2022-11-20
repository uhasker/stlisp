import operator as op


def find_env(env, sym):
    return env if (env is None or sym in env) else find_env(env.get("__outer__", None), sym)


def stlisp_eval(env, expr):
    match expr:
        case int(expr) | float(expr): return expr
        case str(expr): return find_env(env, expr)[expr]
        case ("define", sym, sym_expr): env[sym] = stlisp_eval(env, sym_expr)
        case ("lambda", params, body): return lambda *args: stlisp_eval(dict(zip(params, args)) | {"__outer__": env}, body)
        case ("quote", quote_arg): return quote_arg
        case ("if", test, conseq, alt): return stlisp_eval(env, (conseq if stlisp_eval(env, test) else alt))
        case ("set!", sym, sym_expr): find_env(env, sym)[sym] = stlisp_eval(env, sym_expr)
        case (proc, *args): return stlisp_eval(env, proc)(*[stlisp_eval(env, arg) for arg in args])


global_env = {k: v for k, v in (vars(__builtins__) | vars(op)).items() if callable(v) and not isinstance(v, type)}
global_env |= {"cons": lambda x, y: (x, *y) if isinstance(y, tuple) else (x, y), "car": lambda x: x[0], "cdr": lambda x: x[1:], "prog": lambda *x: x[-1]}

while True: print(stlisp_eval(global_env, eval(input("stlisp> "))))
