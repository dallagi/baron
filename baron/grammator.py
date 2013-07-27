# Ma grammaire en carton

# TODO/TOTEST

### dotted_name: NAME
### dotted_name: NAME.NAME
### dotted_name: NAME([NAME] -> . <- [NAME] NAME)+

### dotted_as_name: dotted_name
### dotted_as_name: dotted_name SPACE -> 'as' <- SPACE NAME

### dotted_as_names: dotted_as_name
### dotted_as_names: dotted_as_name [SPACE] -> ',' <- [SPACE] dotted_as_name
### dotted_as_names: dotted_as_name ([SPACE] -> ',' <- [SPACE] dotted_as_name)*

### import_as_name: NAME
### import_as_name: NAME SPACE -> 'as' <- SPACE NAME

### import_as_names: import_as_name
### import_as_names: import_as_name [SPACE] -> ',' <- [SPACE] import_as_name
### import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)*
### import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)* [SPACE] -> [',']

### import_name: 'import' <- SPACE dotted_as_names

### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- SPACE import_as_names
### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '(' <- [SPACE] import_as_names [SPACE] -> ')'
### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '*'

### import_from: 'from' <- [SPACE] '.'* <- [SPACE] dotted_name SPACE 'import' ...........
### import_from: 'from' <- [SPACE] '.'+ <- [SPACE] 'import' ...........

# -

### global_stmt: 'global' SPACE NAME
### global_stmt: 'global' SPACE NAME ([SPACE] ',' [SPACE] NAME)*

# -

### break_stmt: 'break'
### pass_stmt: 'pass'
### continue_stmt: 'continue'

# -

### yield_stmt: yield_expr

### yield_expr: 'yield'
### yield_expr: 'yield' SPACE [testlist]

# -

# funcdef: 'def' SPACE NAME [SPACE] parameters [SPACE] ':' [SPACE] suite

# -

### should the SPACE really be there?
# parameters: '(' [SPACE] [varargslist] [SPACE] ')'

# -

# varargslist: [SPACE]

# varargslist: fpdef
# varargslist: fpdef [SPACE] '=' [SPACE] test
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ','
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test [SPACE] ','

# varargslist: '*' [SPACE] NAME
# varargslist: '**' [SPACE] NAME
# varargslist: '*' NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '**' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '**' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME

# -

# suite: simple_stmt
# suite: [SPACE] NEWLINE INDENT stmt+ DEDENT

# -

# fpdef: NAME
# fpdef: '(' [SPACE] fplist [SPACE] ')'

# -

# fplist: fpdef
# fplist: fpdef [SPACE] ',' [SPACE] fpdef
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)*
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)* [SPACE] [',']

# -

# decorator: '@' [SPACE] dotted_name [SPACE] NEWLINE
# decorator: '@' dotted_name [ [SPACE] '(' [SPACE] [arglist] [SPACE] ')' ] [SPACE] NEWLINE

# -

# decorators: (decorator [BLANKLINE])+

# -

# decorated: decorators classdef
# decorated: decorators funcdef

# -

### stmt: simple_stmt
# stmt: compound_stmt

# -

### simple_stmt: small_stmt [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

# -

### small_stmt: expr_stmt
### small_stmt: print_stmt
### small_stmt: del_stmt
### small_stmt: pass_stmt
### small_stmt: flow_stmt
### small_stmt: import_stmt
### small_stmt: global_stmt
### small_stmt: exec_stmt
### small_stmt: assert_stmt

# -

### expr_stmt: testlist
### expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# expr_stmt: testlist augassign yield_expr
### expr_stmt: testlist augassign testlist

# -

### augassign: '+='
### augassign: '-='
### augassign: '*='
### augassign: '/='
### augassign: '%='
### augassign: '&='
### augassign: '|='
### augassign: '^='
### augassign: '<<='
### augassign: '>>='
### augassign: '**='
### augassign: '//='

# -

### print_stmt: 'print'
### print_stmt: 'print' SPACE [ test ]
### print_stmt: 'print' SPACE [ test [SPACE] [','] ]
### print_stmt: 'print' SPACE [ test ([SPACE] ',' [SPACE] test)* [SPACE] [','] ]
### print_stmt: 'print' [SPACE] '>>' [SPACE] test
### print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ ]
### print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ [SPACE] [',']]

# -

### del_stmt: 'del' SPACE exprlist

# -

### flow_stmt: break_stmt
### flow_stmt: continue_stmt
### flow_stmt: return_stmt
### flow_stmt: raise_stmt
### flow_stmt: yield_stmt

# -

### return_stmt: 'return'
### return_stmt: 'return' SPACE [testlist]

# -

### yield_stmt: yield_expr

# -

### raise_stmt: 'raise'
### raise_stmt: 'raise' SPACE [test]
### raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test]]
### raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test [[SPACE] ',' [SPACE] test]]]

# -

### exec_stmt: 'exec' SPACE expr
### exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test]
### exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test [[SPACE] ',' [SPACE] test]]

# -

### assert_stmt: 'assert' SPACE test
### assert_stmt: 'assert' SPACE test [[SPACE] ',' [SPACE] test]

# -

# compound_stmt: if_stmt
# compound_stmt: while_stmt
# compound_stmt: for_stmt
# compound_stmt: try_stmt
# compound_stmt: with_stmt
# compound_stmt: funcdef
# compound_stmt: classdef
# compound_stmt: decorated

# -

# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)*
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ['else' SPACE ':' [SPACE] suite]
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)* ['else' SPACE ':' [SPACE] suite]

# -

# while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite
# while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

# for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite
# for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

# try_stmt: 'try' [SPACE] ':' [SPACE] suite 'finally' [SPACE] ':' suite
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite]
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['finally' [SPACE] ':' suite]
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite] ['finally' [SPACE] ':' suite]

# -

# with_stmt: 'with' SPACE with_item [SPACE] ':' [SPACE] suite
# with_stmt: 'with' SPACE with_item ([SPACE] ',' [SPACE] with_item)* [SPACE] ':' [SPACE] suite

# -

# with_item: test
# with_item: test [SPACE 'as' SPACE expr]

# -

# except_clause: 'except' [SPACE test [(SPACE 'as' SPACE | [SPACE] ',' [SPACE]) test]]

# -

# testlist_safe: old_test
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+]
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+ [SPACE] [',']]

# -

# old_test: or_test
# old_test: old_lambdef

# -

# old_lambdef: 'lambda' [SPACE] ':' [SPACE] old_test
# old_lambdef: 'lambda' SPACE [varargslist] [SPACE] ':' [SPACE] old_test

# -

# test: lambdef
### test: or_test
### test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]

# -

### or_test: and_test
### or_test: and_test (SPACE 'or' SPACE and_test)*

# -

### and_test: not_test
### and_test: not_test (SPACE 'and' SPACE not_test)*

# -

### not_test: 'not' SPACE not_test
### not_test: comparison

# -

### comparison: expr
### comparison: expr (comp_op expr)*

# -

### comp_op: '<'
### comp_op: '>'
### comp_op: '=='
### comp_op: '>='
### comp_op: '<='
### comp_op: '<>'
### comp_op: '!='
### comp_op: 'in'
### comp_op: 'not' SPACE 'in'
### comp_op: 'is'
### comp_op: 'is' SPACE 'not'

# -

### expr: xor_expr
### expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*

# -

### xor_expr: and_expr
### xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*

# -

### and_expr: shift_expr
### and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*

# -

### shift_expr: arith_expr
### shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*

# -

### arith_expr: term
### arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*

# -

### term: factor
### term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*

# -

### factor: ('+'|'-'|'~') [SPACE] factor
### factor: power

# -

### power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

# -

# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
# atom: '[' [SPACE] [listmaker] [SPACE] ']'
# atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# atom: '`' [SPACE] testlist1 [SPACE] '`'
### atom: NAME
### atom: NUMBER
### atom: STRING+

# -

# listmaker: test
# listmaker: test [SPACE] list_for
# listmaker: test ([SPACE] ',' [SPACE] test)*
# listmaker: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# testlist_comp: test
# testlist_comp: test [SPACE] comp_for
# testlist_comp: test ([SPACE] ',' [SPACE] test)*
# testlist_comp: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# lambdef: 'lambda' [SPACE] ':' [SPACE] test
# lambdef: 'lambda' [SPACE] [varargslist] [SPACE] ':' [SPACE] test

# -

### trailer: '.' [SPACE] NAME
### trailer: '[' [SPACE] ']'
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
### trailer: '(' [SPACE] ')'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# -

# subscriptlist: subscript
# subscriptlist: subscript [SPACE] [',']
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)*
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)* [SPACE] [',']

# -

# subscript: test
# subscript: '.' [SPACE] '.' [SPACE] '.'
# subscript: [test] [SPACE] ':' [SPACE] [test] [SPACE] [sliceop]

# -

# sliceop: ':' [SPACE] [test]

# -

# exprlist: expr
# exprlist: expr [SPACE] [',']
# exprlist: expr ([SPACE] ',' [SPACE] expr)*
# exprlist: expr ([SPACE] ',' [SPACE] expr)* [SPACE] [',']

# -

# testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE]
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)*)
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)* [SPACE] [','])

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] comp_for

# dictorsetmaker: test [SPACE] comp_for

# dictorsetmaker: test [SPACE]
# dictorsetmaker: test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)*
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# classdef: 'class' SPACE NAME [SPACE] ['(' [SPACE] [testlist] [SPACE] ')'] [SPACE] ':' [SPACE] suite

# -

# for reference
# arglist: (argument [SPACE] ',' [SPACE])* (argument [SPACE] [','] |'*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test] |'**' [SPACE] test)


# arglist: (argument [SPACE] ',' [SPACE])*
# arglist: argument [SPACE] [',']
# arglist: (argument [SPACE] ',' [SPACE])* argument [SPACE] [',']
# arglist: '**' [SPACE] test
# arglist: (argument [SPACE] ',' [SPACE])* '**' [SPACE] test

# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]
# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]

# -

# argument: test
# argument: test [SPACE comp_for]
# argument: test [SPACE] '=' [SPACE] test

# -

# list_iter: list_if
# list_iter: list_for

# -

# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe
# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe [SPACE list_iter]

# -

# list_if: 'if' SPACE old_test
# list_if: 'if' SPACE old_test [SPACE list_iter]

# -

# comp_iter: comp_if
# comp_iter: comp_for

# -

# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# -

# comp_if: 'if' SPACE old_test
# comp_if: 'if' SPACE old_test [SPACE comp_iter]

# -

# testlist1: test
# testlist1: test ([SPACE] ',' [SPACE] test)*

# -

### yield_expr: 'yield'
### yield_expr: 'yield' [SPACE testlist]

# -

# single_input: NEWLINE
# single_input: simple_stmt
# single_input: compound_stmt [SPACE] NEWLINE

# -

# file_input: ([SPACE] NEWLINE | stmt)* [SPACE] ENDMARKER

# -

# eval_input: testlist ([SPACE] NEWLINE)* [SPACE] ENDMARKER

# ---

# KEYWORDS: "and as assert break class continue def del elif else except exec finally for from global if import in is lambda not or pass print raise return try while with yield"

from rply.token import Token
from rply import ParserGenerator

from tokenizer import TOKENS, KEYWORDS, tokenize
from utils import (create_node_from_token, binary_operator, unitary_operator,
                   comparison, boolean_operator, ternary_operator, assignment,
                   augmented_assignment, tuple_)
from grammator_imports import include_imports


pg = ParserGenerator(tuple(map(lambda x: x.upper(), KEYWORDS)) + zip(*TOKENS)[1] + ("ENDMARKER",), cache_id="baron")
        # precedence=[("left", ['PLUS', 'MINUS'])], cache_id="baron")


@pg.production("main : statements")
def main((statements,)):
    return filter(None, statements) if statements else []


@pg.production("statements : statements statement")
def statements_statement((statements, statement)):
    return statements + statement


@pg.production("statements : statement")
def statement((statement,)):
    return statement


@pg.production("statement : ENDMARKER")
def end((endmarker)):
    return [None]


@pg.production("statement : simple_stmt")
def statement_simple_statement((simple_stmt,)):
    return [simple_stmt]


@pg.production("simple_stmt : small_stmt ENDL")
def simple_stmt((small_stmt, endl)):
    return small_stmt


@pg.production("small_stmt : flow_stmt")
@pg.production("small_stmt : del_stmt")
@pg.production("small_stmt : pass_stmt")
@pg.production("small_stmt : assert_stmt")
@pg.production("small_stmt : raise_stmt")
@pg.production("small_stmt : global_stmt")
@pg.production("small_stmt : print_stmt")
def separator((statement,)):
    return statement

include_imports(pg)


@pg.production("print_stmt : PRINT")
def print_stmt_empty((print_,)):
    return {
        "type": "print",
        "value": None,
        "destination": None,
        "destination_space": "",
        "space": "",
    }


@pg.production("print_stmt : PRINT testlist")
def print_stmt((print_, testlist)):
    return {
        "type": "print",
        "value": testlist["value"] if testlist["type"] == "tuple" else [testlist],
        "destination": None,
        "destination_space": "",
        "space": print_.after_space,
    }


@pg.production("print_stmt : PRINT RIGHT_SHIFT test")
def print_stmt_redirect((print_, right_shift, test)):
    return {
        "type": "print",
        "value": None,
        "destination": test,
        "destination_space": right_shift.after_space,
        "space": print_.after_space,
    }


@pg.production("print_stmt : PRINT RIGHT_SHIFT test COMMA testlist")
def print_stmt_redirect_testlist((print_, right_shift, test, comma, testlist)):
    value = []
    if comma.before_space:
        value += [{"type": "space", "value": comma.before_space}]
    value += [create_node_from_token(comma)]
    if comma.after_space:
        value += [{"type": "space", "value": comma.after_space}]
    print testlist
    value += testlist["value"] if testlist["type"] == "tuple" else [testlist]
    return {
        "type": "print",
        "value": value,
        "destination": test,
        "destination_space": right_shift.after_space,
        "space": print_.after_space,
    }


@pg.production("flow_stmt : return_stmt")
@pg.production("flow_stmt : break_stmt")
@pg.production("flow_stmt : continue_stmt")
@pg.production("flow_stmt : yield_stmt")
@pg.production("yield_stmt : yield_expr")
def flow((flow_stmt,)):
    return flow_stmt


@pg.production("return_stmt : RETURN")
@pg.production("yield_expr : YIELD")
def return_empty((token,)):
    return {
        "type": token.name.lower(),
        "value": None,
        "space": ""
    }


@pg.production("break_stmt : BREAK")
@pg.production("continue_stmt : CONTINUE")
@pg.production("pass_stmt : PASS")
def break_stmt((token,)):
    return {"type": token.name.lower()}


@pg.production("raise_stmt : RAISE")
def raise_stmt_empty((raise_,)):
    return {
        "type": "raise",
        "value": None,
        "instance": None,
        "traceback": None,
        "first_space": raise_.after_space,
        "second_space": "",
        "third_space": "",
        "forth_space": "",
        "fith_space": ""
    }


@pg.production("raise_stmt : RAISE test")
def raise_stmt((raise_, test)):
    return {
        "type": "raise",
        "value": test,
        "instance": None,
        "traceback": None,
        "first_space": raise_.after_space,
        "second_space": "",
        "third_space": "",
        "forth_space": "",
        "fith_space": ""
    }


@pg.production("raise_stmt : RAISE test COMMA test")
def raise_stmt_instance((raise_, test, comma, test2)):
    return {
        "type": "raise",
        "value": test,
        "instance": test2,
        "traceback": None,
        "first_space": raise_.after_space,
        "second_space": comma.before_space,
        "third_space": comma.after_space,
        "forth_space": "",
        "fith_space": ""
    }


@pg.production("raise_stmt : RAISE test COMMA test COMMA test")
def raise_stmt_instance_traceback((raise_, test, comma, test2, comma2, test3)):
    return {
        "type": "raise",
        "value": test,
        "instance": test2,
        "traceback": test3,
        "first_space": raise_.after_space,
        "second_space": comma.before_space,
        "third_space": comma.after_space,
        "forth_space": comma2.before_space,
        "fith_space": comma2.after_space
    }


@pg.production("assert_stmt : EXEC expr")
def exec_stmt((exec_, expr)):
    return {
        "type": "exec",
        "value": expr,
        "globals": None,
        "locals": None,
        "first_space": exec_.after_space,
        "second_space": "",
        "third_space": "",
        "forth_space": "",
        "fith_space": ""
    }


@pg.production("assert_stmt : EXEC expr IN test")
def exec_stmt_in((exec_, expr, in_, test)):
    return {
        "type": "exec",
        "value": expr,
        "globals": test,
        "locals": None,
        "first_space": exec_.after_space,
        "second_space": in_.before_space,
        "third_space": in_.after_space,
        "forth_space": "",
        "fith_space": ""
    }


@pg.production("assert_stmt : EXEC expr IN test COMMA test")
def exec_stmt_in_comma((exec_, expr, in_, test, comma, test2)):
    return {
        "type": "exec",
        "value": expr,
        "globals": test,
        "locals": test2,
        "first_space": exec_.after_space,
        "second_space": in_.before_space,
        "third_space": in_.after_space,
        "forth_space": comma.before_space,
        "fith_space": comma.after_space
    }


@pg.production("assert_stmt : ASSERT test")
def assert_stmt((assert_, test)):
    return {
        "type": "assert",
        "value": test,
        "message": None,
        "first_space": assert_.after_space,
        "second_space": "",
        "third_space": ""
    }


@pg.production("assert_stmt : ASSERT test COMMA test")
def assert_stmt_message((assert_, test, comma, test2)):
    return {
        "type": "assert",
        "value": test,
        "message": test2,
        "first_space": assert_.after_space,
        "second_space": comma.before_space,
        "third_space": comma.after_space
    }


@pg.production("global_stmt : GLOBAL names")
def global_stmt((global_, names)):
    return {
        "type": "global",
        "space": global_.after_space,
        "value": names,
    }


@pg.production("names : NAME")
def names_name((name,)):
    return [create_node_from_token(name)]


@pg.production("names : names COMMA NAME")
def names_names_name((names, comma, name,)):
    to_return = names
    if comma.before_space:
        to_return += [{"type": "space", "value": comma.before_space}]
    to_return += [create_node_from_token(comma)]
    if comma.after_space:
        to_return += [{"type": "space", "value": comma.after_space}]
    to_return += [create_node_from_token(name)]
    return to_return


@pg.production("return_stmt : RETURN testlist")
@pg.production("yield_expr : YIELD testlist")
@pg.production("del_stmt : DEL exprlist")
def return_testlist((token, testlist)):
    return {
        "type": token.name.lower(),
        "value": testlist,
        "space": token.after_space,
    }


@pg.production("small_stmt : expr_stmt")
@pg.production("expr_stmt : testlist")
@pg.production("testlist : test")
@pg.production("test : or_test")
@pg.production("or_test : and_test")
@pg.production("and_test : not_test")
@pg.production("not_test : comparison")
@pg.production("comparison : expr")
@pg.production("expr : xor_expr")
@pg.production("xor_expr : and_expr")
@pg.production("and_expr : shift_expr")
@pg.production("shift_expr : arith_expr")
@pg.production("arith_expr : term")
@pg.production("term : factor")
@pg.production("factor : power")
@pg.production("power : atom")
@pg.production("exprlist : expr")
def term_factor((level,)):
    return level


@pg.production("testlist : test testlist_part")
@pg.production("exprlist : expr exprlist_part")
def implicit_tuple((test, testlist_part)):
    return tuple_([test] + testlist_part, with_parenthesis=False)


@pg.production("testlist : test COMMA")
@pg.production("exprlist : expr COMMA")
def implicit_tuple_alone((test, comma)):
    tuple_content = [test]
    if comma.before_space:
        tuple_content += [{"type": "space", "value": comma.before_space}]
    tuple_content += [create_node_from_token(comma)]
    return tuple_(tuple_content, with_parenthesis=False)


@pg.production("testlist_part : COMMA test COMMA?")
@pg.production("exprlist_part : COMMA expr COMMA?")
def testlist_part((comma, test, comma2)):
    to_return = []
    if comma.before_space:
        to_return += [{"type": "space", "value": comma.before_space}]
    to_return += [create_node_from_token(comma)]
    if comma.after_space:
        to_return += [{"type": "space", "value": comma.after_space}]
    to_return += [test]
    if comma2 and comma2.before_space:
        to_return += [{"type": "space", "value": comma2.before_space}]
    if comma2:
        to_return += [create_node_from_token(comma2)]
    return to_return


@pg.production("testlist_part : COMMA test testlist_part")
@pg.production("exprlist_part : COMMA expr exprlist_part")
def testlist_part_next((comma, test, testlist_part)):
    to_return = []
    if comma.before_space:
        to_return += [{"type": "space", "value": comma.before_space}]
    to_return += [create_node_from_token(comma)]
    if comma.after_space:
        to_return += [{"type": "space", "value": comma.after_space}]
    to_return += [test] + testlist_part
    return to_return


@pg.production("expr_stmt : testlist PLUS_EQUAL testlist")
@pg.production("expr_stmt : testlist MINUS_EQUAL testlist")
@pg.production("expr_stmt : testlist STAR_EQUAL testlist")
@pg.production("expr_stmt : testlist SLASH_EQUAL testlist")
@pg.production("expr_stmt : testlist PERCENT_EQUAL testlist")
@pg.production("expr_stmt : testlist AMPER_EQUAL testlist")
@pg.production("expr_stmt : testlist VBAR_EQUAL testlist")
@pg.production("expr_stmt : testlist CIRCUMFLEX_EQUAL testlist")
@pg.production("expr_stmt : testlist LEFT_SHIFT_EQUAL testlist")
@pg.production("expr_stmt : testlist RIGHT_SHIFT_EQUAL testlist")
@pg.production("expr_stmt : testlist DOUBLE_STAR_EQUAL testlist")
@pg.production("expr_stmt : testlist DOUBLE_SLASH_EQUAL testlist")
def augmented_assignment_node((target, operator, value)):
    return augmented_assignment(operator.value[:-1], value, target, operator.before_space, operator.after_space)


@pg.production("expr_stmt : testlist EQUAL expr_stmt")
def assignment_node((target, equal, value)):
    return assignment(value, target, equal.before_space, equal.after_space)


@pg.production("test : or_test IF or_test ELSE test")
def ternary_operator_node((first, if_, second, else_, third)):
    return ternary_operator(
        second,
        first=first,
        second=third,
        first_space=if_.before_space,
        second_space=if_.after_space,
        third_space=else_.before_space,
        forth_space=else_.after_space,
    )


@pg.production("or_test : not_test OR or_test")
@pg.production("and_test : not_test AND and_test")
def and_node((first, operator, second)):
    return boolean_operator(
        operator.value,
        first=first,
        second=second,
        first_space=operator.before_space,
        second_space=operator.after_space,
    )


@pg.production("not_test : NOT not_test")
def not_node((not_, comparison)):
    return unitary_operator('not', target=comparison, space=not_.after_space)


@pg.production("comparison : expr LESS comparison")
@pg.production("comparison : expr GREATER comparison")
@pg.production("comparison : expr EQUAL_EQUAL comparison")
@pg.production("comparison : expr LESS_EQUAL comparison")
@pg.production("comparison : expr GREATER_EQUAL comparison")
@pg.production("comparison : expr LESS_GREATER comparison")
@pg.production("comparison : expr NOT_EQUAL comparison")
@pg.production("comparison : expr IN comparison")
@pg.production("comparison : expr IS comparison")
def comparison_node((expr, comparison_operator, comparison_)):
    return comparison(comparison_operator.value,
                      first=expr,
                      second=comparison_,
                      first_space=comparison_operator.before_space,
                      second_space=comparison_operator.after_space
                      )


@pg.production("comparison : expr IS NOT comparison")
@pg.production("comparison : expr NOT IN comparison")
def comparison_advanced_node((expr, comparison_operator, comparison_operator2, comparison_)):
    return comparison(comparison_operator.value + " " + comparison_operator2.value,
                      first=expr,
                      second=comparison_,
                      first_space=comparison_operator.before_space,
                      second_space=comparison_operator2.after_space,
                      middle_space=comparison_operator.after_space,
                      )


@pg.production("expr : xor_expr VBAR expr")
@pg.production("xor_expr : and_expr CIRCUMFLEX xor_expr")
@pg.production("and_expr : shift_expr AMPER and_expr")
@pg.production("shift_expr : arith_expr RIGHT_SHIFT shift_expr")
@pg.production("shift_expr : arith_expr LEFT_SHIFT shift_expr")
@pg.production("arith_expr : term PLUS arith_expr")
@pg.production("arith_expr : term MINUS arith_expr")
@pg.production("term : factor STAR term")
@pg.production("term : factor SLASH term")
@pg.production("term : factor PERCENT term")
@pg.production("term : factor DOUBLE_SLASH term")
@pg.production("power : atom DOUBLE_STAR factor")
@pg.production("power : atom DOUBLE_STAR power")
def binary_operator_node((first, operator, second)):
    return binary_operator(
        operator.value,
        first,
        second,
        first_space=operator.before_space,
        second_space=operator.after_space
    )


@pg.production("factor : PLUS factor")
@pg.production("factor : MINUS factor")
@pg.production("factor : TILDE factor")
def factor_unitary_operator_space((operator, factor,)):
    return unitary_operator(operator.value, factor, space=operator.after_space)


@pg.production("power : atomtrailers DOUBLE_STAR factor")
@pg.production("power : atomtrailers DOUBLE_STAR power")
def power_atomtrailer_power((atomtrailers, double_star, factor)):
    return binary_operator(
        double_star.value,
        {
            "type": "atomtrailers",
            "value": atomtrailers,
        },
        factor,
        first_space=double_star.before_space,
        second_space=double_star.after_space
    )


@pg.production("power : atomtrailers")
def power_atomtrailers((atomtrailers,)):
    return {"type": "atomtrailers", "value": atomtrailers}


@pg.production("atomtrailers : atom")
def atomtrailers_atom((atom,)):
    return [atom]


@pg.production("atomtrailers : atom trailers")
def atomtrailer((atom, trailers)):
    return [atom] + trailers


@pg.production("trailers : trailer")
def trailers((trailer,)):
    return trailer


@pg.production("trailers : trailers trailer")
def trailers_trailer((trailers, trailer)):
    return trailers + trailer


@pg.production("trailer : DOT NAME")
def trailer((dot, name,)):
    to_return = []
    if dot.before_space:
        to_return += [{"type": "space", "value": dot.before_space}]
    to_return += [create_node_from_token(dot)]
    if dot.after_space:
        to_return += [{"type": "space", "value": dot.after_space}]
    to_return += [create_node_from_token(name)]
    return to_return


@pg.production("trailer : LEFT_SQUARE_BRACKET RIGHT_SQUARE_BRACKET")
@pg.production("trailer : LEFT_PARENTHESIS RIGHT_PARENTHESIS")
def trailer_getitem((left, right)):
    to_return = []
    if left.before_space:
        to_return += [{"type": "space", "value": left.before_space}]
    to_return += [{"type": "getitem" if left.value == "[" else "call", "value": None, "first_space": left.after_space, "second_space": ""}]
    return to_return


@pg.production("atom : INT")
def int((int_,)):
    return create_node_from_token(int_, section="number")


@pg.production("atom : NAME")
def name((name,)):
    return create_node_from_token(name)


@pg.production("atom : STRING")
def string((string_,)):
    return create_node_from_token(string_)

parser = pg.build()


def fake_lexer(sequence):
    for i in tokenize(sequence):
        if i is None:
            yield None
        yield Token(*i)


def parse(sequence):
    return parser.parse(fake_lexer(sequence))

if __name__ == '__main__':
    import json
    from grouper import group
    from spliter import split

    def pouet(sequence):
        return tokenize(group(split(sequence)))

    def pouetpouet(sequence):
        return group(split(sequence))

    def pouetpouetpouet(sequence):
        for i in sequence:
            if i is None:
                yield None
            yield Token(*i)

    # print pouet('1')
    print json.dumps(parse(pouetpouet('a and b and c')), indent=4, sort_keys=True)
    # print json.dumps(parser.parse(pouetpouetpouet([('ENDMARKER', ''), None])), indent=4)
