# Map
ROOMS = {
    'Clear Grounds': {'North': 'Castle Gardens', 'East': 'Mythical Armoury'},
    'Mythical Armoury': {'West': 'Clear Grounds', 'Item': 'Sword'},
    'Castle Gardens': {'North': 'Castle Gates', 'South': 'Clear Grounds'},
    'Castle Gates': {'East': 'Castle Main Hall', 'South': 'Castle Gardens'},
    'Castle Main Hall': {'South': 'Royal Chambers',
                         'West': 'Castle Gates', 'East': 'Castle Kitchens'},
    'Royal Chambers': {'North': 'Castle Main Hall', 'Madking': 'The Mad King'},
    'Castle Kitchens': {'South': 'Castle Storage', 'West': 'Castle Main Hall'},
    'Castle Storage': {
        'North': 'Castle Kitchens',
        'Item': 'Magical Armour', 'Witch': 'The Kitchen Witch'
    }
}
