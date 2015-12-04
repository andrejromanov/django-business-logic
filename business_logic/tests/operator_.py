# -*- coding: utf-8 -*-
#


from django.test import TestCase
from ..models import *



class BinaryOperatorTest(TestCase):
    def test_init(self):
        add_operator = BinaryOperator(operator='+')
        self.failUnlessEqual('+', add_operator.operator)

    def test_raise_on_incorrect_operator(self):
        self.failUnlessRaises(TypeError, BinaryOperator, **dict(operator='z'))
        operator = BinaryOperator(operator='+')
        operator.operator = 'z'
        self.failUnlessRaises(TypeError, operator.save)

    def test_str(self):
        add_operator = BinaryOperator(operator='+')
        self.failUnlessEqual('+', str(add_operator))

    def test_interpret_mod(self):
        mod_operator = BinaryOperator(operator='%')
        integer_const1 = IntegerConstant(value=11)
        integer_const2 = IntegerConstant(value=3)
        ctx = Context()
        result = mod_operator.interpret(ctx, integer_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual(11 % 3, result)

        string_const1 = StringConstant(value='x%s')
        result = mod_operator.interpret(ctx, string_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual('x3', result)

    def test_interpret_add(self):
        add_operator = BinaryOperator(operator='+')
        integer_const1 = IntegerConstant(value=5)
        integer_const2 = IntegerConstant(value=6)
        ctx = Context()
        result = add_operator.interpret(ctx, integer_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual(5 + 6, result)

        float_const1 = FloatConstant(value=1.2)
        float_const2 = FloatConstant(value=2.3)
        ctx = Context()
        result = add_operator.interpret(ctx, float_const1.interpret(ctx),
                float_const2.interpret(ctx))
        self.failUnlessEqual(1.2 + 2.3, result)

    def test_interpret_sub(self):
        sub_operator = BinaryOperator(operator='-')
        integer_const1 = IntegerConstant(value=5)
        integer_const2 = IntegerConstant(value=6)
        ctx = Context()
        result = sub_operator.interpret(ctx, integer_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual(5 - 6, result)

        float_const1 = FloatConstant(value=1.2)
        float_const2 = FloatConstant(value=2.3)
        ctx = Context()
        result = sub_operator.interpret(ctx, float_const1.interpret(ctx),
                float_const2.interpret(ctx))
        self.failUnlessEqual(1.2 - 2.3, result)

    def test_interpret_mul(self):
        mul_operator = BinaryOperator(operator='*')
        integer_const1 = IntegerConstant(value=2)
        integer_const2 = IntegerConstant(value=3)
        ctx = Context()
        result = mul_operator.interpret(ctx, integer_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual(2 * 3, result)

        float_const1 = FloatConstant(value=1.2)
        float_const2 = FloatConstant(value=2.3)
        ctx = Context()
        result = mul_operator.interpret(ctx, float_const1.interpret(ctx),
                float_const2.interpret(ctx))
        self.failUnlessEqual(1.2 * 2.3, result)

    def test_interpret_div(self):
        div_operator = BinaryOperator(operator='/')
        integer_const1 = IntegerConstant(value=2)
        integer_const2 = IntegerConstant(value=3)
        ctx = Context()
        result = div_operator.interpret(ctx, integer_const1.interpret(ctx),
                integer_const2.interpret(ctx))
        self.failUnlessEqual(2 / 3, result)

        float_const1 = FloatConstant(value=1.2)
        float_const2 = FloatConstant(value=2.3)
        ctx = Context()
        result = div_operator.interpret(ctx, float_const1.interpret(ctx),
                float_const2.interpret(ctx))
        self.failUnlessEqual(1.2 / 2.3, result)


class UnaryOperatorTest(TestCase):
    def test_init(self):
        neg_operator = UnaryOperator(operator='-')
        self.failUnlessEqual('-', neg_operator.operator)

    def test_str(self):
        neg_operator = UnaryOperator(operator='-')
        self.failUnlessEqual('-', str(neg_operator))

    def test_interpret_neg(self):
        neg_operator = UnaryOperator(operator='-')
        integer_const1 = IntegerConstant(value=3)
        ctx = Context()
        result = neg_operator.interpret(ctx, integer_const1.interpret(ctx))
        self.failUnlessEqual(-(3), result)
