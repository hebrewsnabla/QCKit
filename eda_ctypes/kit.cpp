#include<iostream>
#include<set>
//#include<iterator>
using namespace std;

set<int> reduce(int *atombegin, int *atomend)
{
    set<int> inter_item(atombegin, atomend);
    //for (int const& atom : inter_item)
    //{
    //    cout << atom << ' ';
    //}
    return inter_item;
}

void get_inter(int nao)
{
    for (int i=1; i++; nao)
        for (int j=1; j++; nao)
            for (int k=1; k++; nao)
                for (int l=1; l++; nao)
                {
                    int atom4 = {i, j, k, l};
                    int *abegin = begin(atom4);
                    int *aend = end(atom4);
                    set<int> inter_item = reduce(abegin, aend);
                    for (int const& atom : inter_item)
                        cout << atom << ' ';
                    cout << '\n';
                }
}

int main()
{
    //int a[] = {3,4,1,1};
    //int *abegin = begin(a);
    //int *aend = end(a);
    //reduce(abegin, aend);
    get_inter(10);
    return 0;
}

