// =====================================================================================
//
//       Filename:  jmp-linear.c
//
//    Description:  setjmp() / longjmp()
//
//        Version:  1.0
//        Created:  2014-09-22 22:09:18
//       Revision:  none
//       Compiler:  g++
//
//         Author:  SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
//        Company:
//
// =====================================================================================

#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

jmp_buf task1;
jmp_buf task2;

void func2(int n)
{
    if (!setjmp(task2))
    {
        printf("task2, setjmp() => %d, %x\n", n, &n);
        longjmp(task2, 1);
    }
    else
    {
        printf("task2, back => %d, %x\n", n, &n);
    }
}

void func1(int n)
{
    if (!setjmp(task1))
    {
        printf("task1, setjmp() => %d, %x\n", n, &n);
        longjmp(task1, 1);
    }
    else
    {
        printf("task1, back => %d, %x\n", n, &n);
        func2(n);
    }

}

int main(int argc, char **argv)
{
    func1(99);

    return EXIT_SUCCESS;
}
