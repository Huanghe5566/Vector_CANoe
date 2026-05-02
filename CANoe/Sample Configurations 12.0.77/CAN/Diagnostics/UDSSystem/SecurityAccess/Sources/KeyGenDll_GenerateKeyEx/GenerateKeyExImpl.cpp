// KeyGeneration.cpp : Defines the entry point for the DLL application.
//

#include <windows.h>
#include "KeyGenAlgoInterfaceEx.h"



BOOL APIENTRY DllMain(HANDLE hModule,
	DWORD  ul_reason_for_call,
	LPVOID lpReserved
)
{
	return TRUE;
}



KEYGENALGO_API VKeyGenResultEx GenerateKeyEx(
	const unsigned char*  iSeedArray,     /* Array for the seed [in] */
	unsigned int          iSeedArraySize, /* Length of the array for the seed [in] */
	const unsigned int    iSecurityLevel, /* Security level [in] */
	const char*           iVariant,       /* Name of the active variant [in] */
	unsigned char*        ioKeyArray,     /* Array for the key [in, out] */
	unsigned int          iKeyArraySize,  /* Maximum length of the array for the key [in] */
	unsigned int&         oSize           /* Length of the key [out] */
)
{
	if (iSeedArraySize > iKeyArraySize)
		return KGRE_BufferToSmall;

/*  以下是原示例 key = seed 方法
	for (unsigned int i = 0; i < iSeedArraySize; i++)
		ioKeyArray[i] = ~iSeedArray[i];
*/

	unsigned int seed = 0;
	unsigned int key = 0;

	seed = iSeedArray[1];   // 将种子 seed 从参数复制到一个整数
	seed = seed | (iSeedArray[0]);    // 种子数组中的字节顺序等于总线消息中的字节顺序

	// 从种子开始计算密钥
	// 使用服务 27 01  - 》 27 02 进行安全访问

	if (iSecurityLevel == 0x01)
	{
		key = seed + 8;
	}
	// 结束从种子计算密钥
	//将密钥复制到输出缓冲区
	ioKeyArray[1] = key & 0xff;
	ioKeyArray[0] = (key >> 8 ) & 0xff;

	oSize = iSeedArraySize;
	return KGRE_Ok;
}


