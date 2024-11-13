# Snippet for Tokens

import ply.lex as lex

# List of token names
tokens = [
    'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'IF', 'ELSE', 'WHILE', 'PRINT', 'ID', 'ASSIGN',
]

# Regular expressions for tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY= r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_IF      = r'IF'
t_ELSE    = r'ELSE'
t_WHILE   = r'WHILE'
t_PRINT   = r'PRINT'

# Rules for numbers and identifiers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Rule for ignoring spaces and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# -------------------------------------------------- #
# Tokens Definitions in PLY

# List of token names
tokens = [
    'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO',
    'ASSIGN', 'EQUAL', 'NOT_EQUAL', 'GREATER', 'LESS', 
    'GREATER_EQUAL', 'LESS_EQUAL', 'AND', 'OR', 'NOT', 
    'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
    'DOT', 'ID'
] + list(reserved.values())

# Reserved words dictionary (for keywords)
reserved = {
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'FOR': 'FOR',
    'SWITCH': 'SWITCH',
    'CASE': 'CASE',
    'DEFAULT': 'DEFAULT',
    'BREAK': 'BREAK',
    'CONTINUE': 'CONTINUE',
    'RETURN': 'RETURN',
    'INT': 'INT',
    'FLOAT': 'FLOAT',
    'STRING': 'STRING',
    'BOOL': 'BOOL',
    'NULL': 'NULL',
    'PRINT': 'PRINT',
    'PRINT_R': 'PRINT_R',
    'VAR_DUMP': 'VAR_DUMP',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT'
}

# Regular expressions for the operators and symbols
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE   = r'/'
t_MODULO   = r'%'
t_ASSIGN   = r'='
t_EQUAL    = r'=='
t_NOT_EQUAL= r'!='
t_GREATER  = r'>'
t_LESS     = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL    = r'<='
t_AND      = r'&&'
t_OR       = r'\|\|'
t_NOT      = r'!'
t_SEMICOLON= r';'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_DOT      = r'\.'

# Define ID token to handle keywords
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t