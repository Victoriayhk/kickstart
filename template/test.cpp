#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;

typedef double DB;
typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<PII> VPII;

// 数组操作
#define PB push_back
#define MP make_pair

// 比大小
template <class T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template <class T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

// 求逆, 快速幂, 组合数, 模内四则运算, 级数
// const int MOD = 1000000007;
// LL inv(LL a) { return a == 1 ? 1 : (MOD - MOD / a) * inv(MOD % a) % MOD; }
// LL mPow(LL x, int n) { LL ret = 1; while (n) { if (n & 1) ret = ret * x % MOD; x = x * x % MOD; n >>= 1; } return ret; }
// LL mC(int n, int m) { LL ret = 1; for(int i = 1; i <= m; i++, n--) { ret = ret * n % MOD * inv(i) % MOD; } return ret; }
// LL add(LL a, LL b) { return (a+b)%MOD; }
// LL minus(LL a, LL b) { return (a+MOD-b)%MOD; }
// LL times(LL a, LL b) { return a*b%MOD; }
// LL divide(LL a, LL b) { return a*inv(b)%MOD; }
// LL uni_sum(LL n) { return n*(n+1)/2%MOD; } // 1 + 2 + ... + n
// LL square_sum2(LL n) { return n*(n+1)%MOD*(2*n+1)%MOD*inv(6)%MOD; } // 1^2 + 2^2 + ... + n^2
// LL cube_sum3(LL n) { return n*n%MOD*(n+1)%MOD*(n+1)%MOD*inv(4)%MOD; } // 1^3 + 2^3 + ... + n^3

// 东南西北四个方向
// const int dx[] = {0, 1, 0, -1};
// const int dy[] = {1, 0, -1, 0};

// 质数筛选, O(n)级
// VI primes;
// bool non_prime[N];
// void get_primes(int n) {
//     primes.PB(2);
//     non_prime[2] = true;
//     for (int i = 2; i < n; i++) {
//         if (!non_prime[i]) primes.PB(i);
//         for (int j = 0; j < (int)primes.size(); j++) {
//             int w = i * primes[j];
//             if (w >= n) break;
//             if (!non_prime[w]) non_prime[w] = true;
//             if (i%primes[j] == 0) break;
//         }
//     }
// }

///////////////////////////////////////////////////////////////////////////////////////

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);

    printf("hello world\n");

    // int T; cin >> T; for (int cas=0; cas < T; cas++) {
    //     int ans = -1;
    //     printf("Case #%d: %d\n", cas+1, ans);
    // }
    return 0;
}