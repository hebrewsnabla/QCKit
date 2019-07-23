#include<iostream>
#include<fstream>
#include<set>
//#include<iterator>
using namespace std;

extern "C" {
void ecoul(double *dm, int nao, double *eri, int *bas2atm, int natom/*, double *ecoul, int necoul*/
);
}

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
    for (int i=1; i<nao; i++)
        for (int j=1; j<nao; j++)
            for (int k=1; k<nao; k++)
                for (int l=1; l<nao; l++)
                {
                    int atom4[] = {i, j, k, l};
                    int *abegin = begin(atom4);
                    int *aend = end(atom4);
                    set<int> inter_item = reduce(abegin, aend);
                    for (int const& atom : inter_item)
                        cout << atom << ' ';
                    cout << '\n';
                }
}

/*
int get_bas2atm(int nao, int *basrg, int natom, int bas_ofatom)
{
    for (int i=1; i<=nao; i++)
    {
        for (int j; j<= natom; j++)
        {
            for (int k; k<= bas_ofatom; k++)
            {
                if ( i ==basrg[(j-1)*natom+k-1])
                {}
            }
        }
        if
    } 
    return bas2atm, bas_num;
}*/

void ecoul(double **dm, int nao, double ****eri, int *bas2atm, int natom/*, double *ecoul, int necoul*/
)
{
    //ofstream f ("1.txt", ios::out);
    //cout << dm[0] << '\n';
    //cout << nao << '\n';
    //cout << eri[0] << '\n';
    double atom_E[natom] = {0.0};
    int ctr = 0;
    #pragma omp parallel for public(bas2atm) reduction(+:atom_E)
    for (int i=0; i < nao; i++)
    {
		for (int j=0; j < nao; j++)
        {
            int dmij = dm[i][j];
            int a = bas2atm[i];
            int b = bas2atm[j];
            for (int k=0; k<nao; k++)
            {
                for (int l=0; l<nao; l++)
                {
                    double ecoul = 0.5 * dmij * dm[k][l] * \
                    (eri[i][j][l][k] - 0.5 * eri[i][k][l][j]);
                    int c = bas2atm[k];
                    int d = bas2atm[l];
                    int abcd[] = {a,b,c,d};
                    int *abegin = begin(abcd);
                    int *aend = end(abcd);
                    set<int> inter_item(abegin, aend);
                    int m = inter_item.size();
                    for (int atom : inter_item)
                    {
                        //f << atom << ' ';
                        atom_E[atom-1] += ecoul/float(m);
                        
                    }
                    //f << '\n';
                    //ctr += 1;
                    
                }
                //break;
            }
            //break;

        }
        //break;
    }
    for (int n=1; n<=natom; n++)
        cout << atom_E[n-1] << ' ';
}



void test(double *dm, int nao)
{
    for (int i=1; i<=nao; i++)
    {
        for (int j=1; j<=nao; j++)
        {
            cout << dm[(i-1)*nao+j-1] << ' ';
        }
        cout << '\n';
    }
}



/*
int main()
{
    //int a[] = {3,4,1,1};
    //int *abegin = begin(a);
    //int *aend = end(a);
    //reduce(abegin, aend);
    
    //get_inter(10);
    return 0;
}
*/
