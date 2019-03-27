def what_are_kwargs( *args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(1,2,3,4,5, booze=3, pilot="steve")