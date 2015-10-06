_negs = [

    # facebook

    '2008/fbml',
    'like.php',
    'sharer.php',
    'likebox.php',
    '/plugins/',

    # twitter

    '/intent/',
    '?status=',
    'twitter.com/share',
    'widgets.js',
    '/widgets/',

    # g+

    '/share?',

    # pinterest

    'pinit.js',
    'pin/create',
    'pinmarklet.js',

]

_negs_equals = [
    'facebook.com',
    'twitter.com',
    'facebook.com/',
    'twitter.com/',
]

social = [
    'facebook.com',
    'twitter.com',
    'plus.google.com',
    'pinterest.com',
    'youtube.com',
]

amazon = [
    'amazon.com.au',
    'amazon.com.br',
    'amazon.ca',
    'amazon.cn',
    'amazon.fr',
    'amazon.de',
    'amazon.in',
    'amazon.it',
    'amazon.co.jp',
    'amazon.com.mx',
    'amazon.nl',
    'amazon.es',
    'amazon.co.uk',
    'amazon.com/',
]

advertising = [
    'google_ad_client',
    'doubleclick.net',
]

analytics = [
    'google-analytics.com/ga.js',
    'googletag', #webmaster

    'connect.facebook.net',
    'fb:page_id',
    'fb:app_id',
    'fb:admins',

    'alexa.com',

    'optimizely.com',

]

cms = [

    # Blog
    
    'wordpress',
    'drupal',
    'joomla',

    'expressionengine',
    
    # Wiki

    'mediawiki',
    'phpwiki',
    'tiki wiki',
    'dokuwiki',
    
    # Forum

    'vbulletin',
    'phpbb',
    'mybb',
    'invision',
    'xenforo',

    # Ecommerce

    'magento',
    'prestashop',
    'oscommerce',
    
    'woocommerce',
    'woothemes',

]

dictionary = [ 

    # Finance / Law

    'debt',
    'saving',
    'mortgage',
    'insurance',
    'financ',  
    'pay',
    'tax',
    'money',
    'bank',
    'paid',
    'capital',
    'wealth',

    # Investing

    'invest',

    'forex',
    'binary',
    'stock',
    'equity',

    'gold',
    'metal',
    'silver',

    'trade',
    'trading',

    'crypto',
    'bitcoin',
    'coin',

    # Borrowing

    'loan',  
    'credit',
    'card',

    # Law

    'law',
    'legal',
    'attorney',
    'dui',
    'criminal',




    # Business

    'biz',
    'business',
    'sales',
    'market',
    'manage',
    'work',
    'leader',
    'job',

    # Providers

    'solution',
    'service',
    'consult',
    'pro',
    'strateg',
    'entertain',
    'studio',
    'firm',
    'special',
    'advisor',

    'guru',
    'amateur',
    'coach',
    
    'vip',


    # Entities / Entity

    'llc',
    'inc',
    'corp',
    'partner',
    'associat',
    'club',
    'foundation',
    'group',
    'company',
    'team',
    'gang',
    'alliance',

    # Occupations

    'plumb',
    'floor',
    'construct',
    'contract',
    'security', #security provider
    'build',
    'repair',

    'glass',
    'lumber',
    'wood',


    # Creative / Arts

    'music',
    'dj',
    'song',

    'artist',

    'photo',
    'guitar',
    'poetry',
    'dance',
    'film',

    'visual',

    'production',





    # Fashion

    'fashion',
    'outfit',
    'cloth',





    # Health

    'health',  
    'life',
    'beauty',
    'beauti',

    'juice',
    'smoothie',
    'yogurt',

    'organic',

    'nutri',

    'skin',
    'face',
    'facial',
    'hair',
    'energy',
    'power',

    # Medical

    'chiro',
    'ortho',
    'pedic',

    'medic',

    'doctor',
    'therapy',  
    'massage',
    'clinic',
    'pharma',
    'drug',

    'vision',

    'dental',
    'dentist',

    # Natural

    'natural',

    # Fitness

    'fit',
    'training',
    'yoga',
    'gym',





    # Sports / Gaming

    'sport',

    'golf',
    'horse',
    
    'bike',
    'biking',
    'cycle',
    
    'race',
    'racing',
    'tennis',
    'fish',
    'kayak',
    'diving',
    'surf',
    'ball',
    'hiking',
    'board',

    'sail',
    'marine',

    'game',
    'gaming',

    'play',




    # Auto / Home / Boat

    'car',
    'auto',  
    'motor',

    'estate',  
    'realty',
    'realtor',

    'home',
    'land',
    'property',
    'propertie',
    'prop',
    'house',
    'acre',
    'villa',

    'apt',
    'apartment',
    
    'rent',
    'condo',
    'shore',
    'lake',
    'forest',
    'trail',

    'north',
    'south',
    'east',
    'west',

    'boat',





    # Wedding

    'wedding',
    'marriage',
    'marry',
    'husband',
    'wife',
    'relationship',





    # Students

    'student',
    'college',
    'school',
    'university',
    'education',
    'tutor',
    'learn',
    'academ',
    'instit',
    'study',
    'studies',




    # Lifestyle

    'good',
    'living',
    'diy',
    'freedom',
    'well',

    'country',
    'southern',

    # Travel

    'travel',
    'tour',
    'holiday',
    'voyage',
    'trip',
    'island',
    'vacation',
    
    'flight',
    'fly',

    'backpack',
    
    # Family / Demographics

    'family',

    'mom',
    'mum',
    'mama',
    'dad',
    'parent',

    'kid',
    'child',
    'baby',
    'toddler',

    'senior',
    'elder',
    'youth',
    'young',

    'girl',
    'boy',
    'guy',
    'dude',

    'sister',
    'brother',

    # Outdoor
    
    'outdoor',
    'outside',
    'camp',
    'nature',

    # Food / Beverage

    'food',
    'cook',
    'drink',

    'coffee',
    'pizza',
    'beer',
    'bbq', 
    'wine',
    'grill',
    'cake',
    'burger',

    'cafe',
    'restaurant',

    'eat',
    'eating',
    'eats',

    'recipe',

    # Periodicals

    'magazine',
    'mag',
    'podcast',
    'news',
    'journal',
    'radio',
    'times',
    'press',
    'post',
    'wire',
    'chronic',

    # Gender

    'men',
    'man',

    # Ministry

    'ministry',
    'faith',
    'god',
    'church',
    'scripture',
    'christian',
    'pray',
    'temple',
    'chapel',
    'bible',

    # Activities

    'garden',
    'festiv',
    
    'cinema',
    'theater',
    'theatre',

    'salon',
    'spa',

    # Weed

    '420',
    'weed',
    'marijuana',
    'canna',
    'cannabis',








    # Shopping

    'mall',
    'shop',
    'retail',
    'depot',
    'store',
    'mart',
    'suppl',

    # Books

    'book',
    'fiction',
    'publish',
    'author',

    # Jewlry

    'jewel',
    'jewlry',
    'jeweler',
    'diamond',
    'ring',
    'necklace',

    # Products

    'shoe',
    'vape',

    'kitchen',

    'flower',




    # Web / Tech

    'web',
    'internet',
    'app',
    'tech',
    'online',
    'computer',
    'pc',
    'phone',
    'software',

    # Providers

    'host',
    'seo',
    'design',
    'develop',

    # Platforms

    'wiki',
    'pedia',

    'cms',
    'blog',
    'download',
    'tube',
    'image',
    'video',
    'forum',
    'article',
    'guide',
    'movie',
    'tv',
    'comic',
    'feed',
    'chat',
    'chan',
    'report',
    'gallery',
    'anime',
    'history',
    'planet',
    'buzz',

    'wallpaper',
    'background',

    'hd',

    # Technologies

    'linux', 
    'cloud',
    
    'wordpress',
    'wp',
    'theme',

    'magento',  

    'android',
    'mobile',
    'mobi',
    
    'digi',

    'google',
    'youtube',
    'facebook',





    # Accomodations

    'inn',
    'hotel',
    'motel',
    'booking',
    'lodge',
    'resort',
    'suite',




    # Animals / Pets
    'dog',
    'pet',
    'animal',













    # Places

    'america',
    'usa',

    'canada',
    'toronto',
    'ontario',
    
    'local',
    'town',
    'ville',
    'village',

    'japan',
    '-jp',

    'ocean',
    'coast',
    'atlantic',
    'pacific',
    'beach',
    'mountain',

    'earth',

    # New York

    'newyork',
    'nyc',

    # Texas

    'texas',

    'austin',
    'dallas',
    'houston',

    # Philadelphia

    'philly',
    'philadelphia',

    # States

    'michigan',
    'indiana',
    'california',
    'florida',
    'kansas',
    'hawaii',

    # Cities

    'atlanta',
    'milwaukee',
    'london',
    'losangeles',
    'chicago',
    'seattle',
    'denver',
    'boston',
    'memphis',

    'detroit',












    # Commercial Intent

    'coupon',
    'deal',
    'review',
    'save',
    'free',
    
    'buy',
    'sell',
    'new',
    'ship', #ing; (?)
    'discount',
    'custom',
    'best',
    'top',
    'cheap',
    'sale',
    'bad',
    'built',
    'smart', # (?)
    'perfect',
    'dirty',
    'clean',
    'fast',

    'relief',

    # Informational; traffic funnel.

    'howto',
    'problem',
    'tips',
    'answer',
    'solution',
    'help',
    'about',
    'list',
    'ask',
    'advice',
    'support',
    'faq',
    '101',

    # colors

    'red',
    'blue',
    'orange',
    'green',
    'yellow',
    'purple',
    'black',
    'white',

    # days of the week

    'sunday',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',

    # time

    'today',  
    'minute',
    'future',
    'now',

    'daily',
    'week',
    'month',
    'year',

    'day',
    'night',

    'christmas',
    'halloween',
    'blackfriday',
    'valentine',
    'thanksgiving',

    # 5 w
    
    'who',
    'what',
    'when',
    'where',
    'why',








    # adjectives

    'vintage',
    'classic',
    'oriental',
    'bold',
    'big',
    'small',
    'luxury',
    'rich',
    'poor',
    'advance',
    'premium',
    'premier',
    'awesome',
    'cool',
    '247',

    # uncat

    'science',
    'hydro',
    'ology',
    'chem',

    'global',
    'national',
    'world',
    
    'social',
    'media',
    'plus',
    
    'industr',
    'enterprise',
    
    'system',
    'hub',
    'talk',
    'center',
    'centre',

    'creat',
    'connect',

    'essential',

    'hello',

    'love',


]

"""
true_dict = []
with open('/home/johnny/dev/toolbox/dictionaries/words.txt', 'r') as f:
    for line in f:
        l = line.strip()
        if len(l) > 3:
            true_dict.append(l.lower())
"""