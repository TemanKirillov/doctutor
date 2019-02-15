class I:
    from collections import OrderedDict

Param1 = I.OrderedDict((
    ('type', 'Param'),
    ('content', I.OrderedDict((
        ('name', 'a'),
        ('kind', 'POSITIONAL_OR_KEYWORD'),
        ('default', 'default value'),
        ('desc', 'description here')
        ))
    )
))

Param2 = I.OrderedDict((
    ('type', 'Param'),
    ('content', I.OrderedDict((
        ('name', 'number'),
        ('kind', 'POSITIONAL_ONLY'),
        ('default', ''),
        ('desc', '')
        ))
    )
))

Params1 = I.OrderedDict((
    ('type', 'Params'), 
    ('content', I.OrderedDict((
        ('a', Param1),
        ('number', Param2)
        ))
    )
))

Params2 = I.OrderedDict((
    ('type', 'Params'), 
    ('content', I.OrderedDict())
))

Return1 = I.OrderedDict((
    ('type', 'Return'), 
    ('content', 'returning value')
))
