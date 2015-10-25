def eval_loop():
    while True:
        s = raw_input('> ')
        if s == 'done':
            print s_eval
            break
        s_eval = eval(s)
        print s_eval

eval_loop()

