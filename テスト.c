#include <stdio.h>
#include <string.h>

int main() {
    float data = 0.75f;
    unsigned long buff;
    int i;
    char s[35];

    // 4バイトのデータをコピー
    memcpy(&buff, &data, 4);

    // 文字列の末尾に終端文字を入れる
    s[34] = '\0';

    // 32ビット分ループする（31から0まで）
    for (i = 31; i >= 0; i--) {
        // インデックス調整: 31を0番目として扱うため
        // ビット位置を計算
        int bit_pos = 31 - i;

        // 指定の位置に区切りのハイフンを入れる
        // IEEE 754: 符号(1bit), 指数(8bit), 仮数(23bit)
        // 文字列のインデックスで見ると: [0]が符号, [1-8]が指数, [9-31]が仮数
        if (bit_pos == 1 || bit_pos == 9) {
            s[bit_pos - 1] = '-';
        }

        // ビットを取り出して文字に変換
        if ((buff >> i) & 1) {
            s[31 - i + (bit_pos >= 1 ? 1 : 0) + (bit_pos >= 9 ? 1 : 0)] = '1';
        } else {
            s[31 - i + (bit_pos >= 1 ? 1 : 0) + (bit_pos >= 9 ? 1 : 0)] = '0';
        }
    }

    // 結果を表示
    printf("%s\n", s);

    return 0;
}