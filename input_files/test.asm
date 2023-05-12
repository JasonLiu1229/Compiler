main:                                   # @main
        addiu   $sp, $sp, -48
        sw      $ra, 44($sp)                    # 4-byte Folded Spill
        sw      $fp, 40($sp)                    # 4-byte Folded Spill
        move    $fp, $sp
        addiu   $1, $zero, 5
        sw      $1, 36($fp)
        lui     $1, 16128
        sw      $1, 32($fp)
        addiu   $1, $zero, 99
        sb      $1, 28($fp)
        lw      $5, 36($fp)
        lwc1    $f0, 32($fp)
        cvt.d.s $f0, $f0
        lb      $1, 28($fp)
        move    $2, $sp
        sw      $1, 16($2)
        lui     $1, %hi($.str)
        addiu   $4, $1, %lo($.str)
        mfc1    $6, $f1
        mfc1    $7, $f0
        jal     printf
        nop
        lui     $1, %hi($.str.1)
        addiu   $4, $1, %lo($.str.1)
        jal     printf
        nop
        addiu   $2, $zero, 0
        move    $sp, $fp
        lw      $fp, 40($sp)                    # 4-byte Folded Reload
        lw      $ra, 44($sp)                    # 4-byte Folded Reload
        addiu   $sp, $sp, 48
        jr      $ra
        nop
$.str:
        .asciz  "%d; %f; %c"

$.str.1:
        .asciz  " test"