class FormatCountStrings:
    """
    Custom strings for count string formatting.

    Attributes:
        CHAR_STR: String specifying character count
        LINE_STR: String specifying line count
        WORD_STR: String specifying word count
    """
    CHAR_STR = 'Character'
    LINE_STR = 'Line'
    WORD_STR = 'Word'


class HelpMessages:
    """
    Help message strings for command-line arguments.

    Attributes:
        DESCRIPTION (STR): Description for textwarp arguments

        CHAR_COUNT (STR): Help message for --char-count argument
        LINE_COUNT (STR): Help message for --line-count argument
        MFWS (STR): Help message for --mfws argument
        POS_COUNT (STR): Help message for --pos-count argument
        TIME_TO_READ (STR): Help message for --time-to-read argument
        WORD_COUNT (STR): Help message for --word-count argument
    """
    DESCRIPTION = ('Specify the text analysis function to apply to the '
                   'clipboard.')

    CHAR_COUNT = 'count characters'
    LINE_COUNT = 'count lines'
    MFWS = 'get most frequent words'
    POS_COUNT = 'count parts of speech'
    TIME_TO_READ = 'calculate time to read'
    WORD_COUNT = 'count words'

# String printed to prompt the user for any other text
ANY_OTHER_TEXT_STR = 'Any other text? (y/n) (Copy text to clipboard):'

# String printed to prompt the user for the number of most frequent words
ENTER_MFW_COUNT_STR = 'How many most frequent words?'

# String printed when the user does not enter a number
ENTER_NUMBER_STR = 'Please enter a number.'

# String printed when the previous response was invalid
ENTER_VALID_RESPONSE_STR = 'Please enter a valid response.'

# String printed to prompt the user for words per minute
ENTER_WPM_STR = 'How many words per minute?'

# String printed when the user exits the program
EXIT_STR = 'Exiting the program...'

# Set of strings for indicating a negative response
NO_STRS = {'no', 'n'}

# Tuple of tuples for parts of speech tags and their names
POS_TAGS = (('ADJ', 'Adjectives'), ('ADP', 'Adpositions'), ('ADV', 'Adverbs'), 
            ('CONJ', 'Conjunctions'), ('DET', 'Determiners'), 
            ('NOUN', 'Nouns'), ('NUM', 'Numbers'), ('PRT', 'Particles'), 
            ('PRON', 'Pronouns'), ('VERB', 'Verbs'), ('X', 'Other'))

# Integer representing the length of the longest tag name in POS_TAGS
MAX_POS_LENGTH = max(len(tag_pair[1]) for tag_pair in POS_TAGS)

# Tuple of strings for POS tags representing words
POS_WORD_TAGS = ('ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRT', 
                 'PRON', 'VERB')

# Set of strings for exiting the program
QUIT_STRS = {'quit', 'q', 'exit', 'e'}

# Set of strings for indicating an affirmative response
YES_STRS = {'yes', 'y'}
