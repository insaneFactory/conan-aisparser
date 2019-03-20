#include <iostream>

extern "C" {
#include "test_sixbit.h"
}

int main()
{
	test_binfrom6bit();
	test_init_6bit();
	test_get_6bit();
	return 0;
}
