#include <bits/stdc++.h>
#include <cstdlib>
using namespace std;
#define ll long long
#define EL endl

#include <iostream>
#include <vector>

using namespace std;

#ifdef DEBUG
#define dout cout
#else
struct Dummy
{
  template <typename T>
  Dummy&
  operator<< (const T&)
  {
    return *this;
  }
};
Dummy dout;
#endif

template <typename t_v>
void
dbg_print_array_1d (std::vector<t_v> v)
{
  for (const auto& i : v)
  {
    dout << i << ' ';
  }
  dout << '\n';
}



/*
 * @brief partition algorithm based on dp
 * @example f(10, [1, 5, 10], ret) -> ret = [[1*10], [1*5, 5], [5, 5], [10]]
 * */
void
list_change_combinations (int n, std::vector<int> coin_1d, vector<vector<int>>& ret_2d)
{
  std::vector<std::vector<std::vector<int> > > dp_3d (n + 1);

  dp_3d[0].push_back ({}); // empty for 0 coin

  for (int coin : coin_1d)
  {
    for (int cur_coin  = coin; cur_coin <= n; ++cur_coin)
    {
      for (auto combo_1d : dp_3d[cur_coin - coin])
      {
        combo_1d.push_back (coin);
        dp_3d[cur_coin].push_back (combo_1d);
        dbg_print_array_1d(combo_1d);
      }
    }
  }

  ret_2d = dp_3d[n];
}

int
main ()
{
  int target = 10;
  vector<vector<int>> dp_2d;
  std::vector<int> coin_1d = { 1, 5, 10, 50 };
  list_change_combinations (target, coin_1d, dp_2d);

  cout << "\n=== 組合總數: " << dp_2d.size () << " ===\n";
  int count = 1;
  for (const auto& combo : dp_2d)
  {
    cout << "組合 " << count++ << ": ";
    for (int coin : combo)
      cout << coin << " ";
    cout << endl;
  }

  return 0;
}
