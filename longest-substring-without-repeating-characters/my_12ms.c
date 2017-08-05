#include <stdio.h>

/*struct buffer
{
        int data_len;   //长度
        char data[0];  //起始地址

};*/

int lengthOfLongestSubstring(char* s) {
    int exist[127] = {0};
	int start = 0;
    int pos = 0;
    int ascii = 0;
    int maxLen = 0;
    while(*(s+pos) != '\0'){
        ascii = (int)(*(s+pos));
        if (exist[ascii] && start < exist[ascii])
        {
            start = exist[ascii];
        }
        pos++;
        exist[ascii] = pos;
        if (maxLen < (pos - start))
        {
            maxLen = pos - start;
        }
    }

    return maxLen;
}

int main()
{
    char *s = "akhfkshfeowiun,dkjseiw";
    int ret = 0;
    ret = lengthOfLongestSubstring(s);
    printf("ret = %d\n",ret);
}

