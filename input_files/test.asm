func:
    # Function prologue
    addi $sp, $sp, -4      # reserve space for one word on stack
    sw $ra, 0($sp)         # store the return address

    # Function body
    sll $t0, $a0, 1        # $t0 = 2 * x
    add $t0, $t0, $a0      # $t0 = 3 * x
    sll $t1, $a1, 1        # $t1 = 2 * y
    add $t1, $t1, $a1      # $t1 = 3 * y
    add $v0, $t0, $t1      # $v0 = 3 * x + 2 * y

    # Function epilogue
    lw $ra, 0($sp)         # restore the return address
    addi $sp, $sp, 4       # release the space used on stack
    jr $ra                 # jump to the return address