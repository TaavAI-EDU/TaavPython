def subb(*args):

    if len(args) == 1:
        return args[0]
    
    else:
        res = args[0]
        # for i in range(1, len(args)):
        #     res -= args[i]

        res -= sum(args[1:])
        return res
