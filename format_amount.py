# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#-------------------------------------------------------------
# French
#-------------------------------------------------------------

def manageSeparator(amount, digits=0, separator=' '):
    if amount:
        amount_str = str((amount)).split('.')
        #print amount_str
        nb = 0
        amount_format = []
        temp = ''
        for i in reversed(amount_str[0]):
            #print i
            if nb == 3:
                amount_format.append(separator)
                nb = 0
            else :
                nb+=1
            #print amount_format
            amount_format.append(i)
        amount_format.reverse()
        if digits != 0:
            amount_format.append('.')
            amount_format.append(amount_str[1])
        result = ''.join(amount_format)
        return result
