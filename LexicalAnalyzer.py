import ply.lex as lex

# List of token names
tokens = [
    'NUMBER',       # e.g., 10, 20
    'ID',           # e.g., $num1
    'PLUS',         # +
    'MINUS',        # -
    'MULTIPLY',     # *
    'DIVIDE',       # /
    'MODULO',       # %
    'ASSIGN',       # =
    'EQUAL',        # ==
    'NOT_EQUAL',    # !=
    'GREATER',      # >
    'LESS',         # <
    'GREATER_EQUAL',# >=
    'LESS_EQUAL',   # <=
    'SEMICOLON',    # ;
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'STRING',       # "Hello, world!"
]

# Reserved words dictionary for PHP-like keywords
reserved = {
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'PRINT': 'PRINT',
}

# Adding reserved keywords to tokens list
tokens += list(reserved.values())

# Regular expressions for operators and symbols
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Regular expression for a number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regular expression for a string
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove quotation marks
    return t

# Regular expression for an identifier (variable)
def t_ID(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'ID')  # Check for reserved words
    return t

# Ignoring whitespace and tabs
t_ignore = ' \t'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test input for PHP-like script
test_input = '''
PRINT "Hello, world!";
$num1 = 10;
$sum = $num1 + 20;
IF ($num1 > $num2) { PRINT "Num1 is larger"; }
WHILE ($num <= 100) { IF ($num % 2 == 0) { PRINT $num; } $num = $num + 1; }
'''

# Give the lexer input and tokenize
lexer.input(test_input)

# Tokenize and print each token
for tok in lexer:
    print(tok)