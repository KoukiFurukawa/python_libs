#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void MargeSort(int a[], int left, int right);

int main(void){
    int iRandNums[1000001];
}

void MargeSort(int lst[], int left, int right){

    /* 変数宣言 ------------------------------------------------------*/
    int buf[1000010];
    int mid, i, j, iterator_left = 0, iterator_right = right-left-1;

    /* 範囲が1以下の時は何もしない ------------------------------------*/
    if (right - left <= 1){
        return;
    }

    /* 分割していく ------------------------------------------------- */
    mid = (left + right) / 2;
    MargeSort(lst, mid, right);
    MargeSort(lst, left, mid);

    /* 分割し終えたら結合の前準備 ------------------------------------- */
    for (i = left; i < mid; i++){
        buf[i] = lst[i];
    }
    for (j = mid, i = right-1; i >= mid; j++,i--){
        buf[j] = lst[i];
    }

    /* マージする -------------------------------------------------------- */
    for (i = left; i < right; i++){
        
        /* 右端が大きかった場合 -------------------------------------------- */
        if (buf[iterator_left <= buf[iterator_right]]){
            lst[i] = buf[iterator_left++];
        }else{
            lst[i] = buf[iterator_right--];
        }
    }


}