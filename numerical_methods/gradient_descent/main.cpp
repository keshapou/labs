#include <iostream>
#include <cmath>

double derivativeX1(const double &);
double derivativeX2(const double &);

int main()
{
    double step, X1, X2;
    const double E = 0.01;

    std::cout << "Choose the starting point\n";
    std::cout << "X1: "; std::cin >> X1;
    std::cout << "X2: "; std::cin >> X2;
    std::cout << "Choose the step: "; std::cin >> step;

    size_t it = 0;

    while ( fabs(derivativeX1(X1)) >= E || fabs(derivativeX2(X2)) >= E )
    {
        X1 = X1 - step * derivativeX1(X1);
        X2 = X2 - step * derivativeX2(X2);
        ++it;

        std::cout << it << " X1 = " << X1 << '\t';
        std::cout << it << " X2 = " << X2 << std::endl;

    }

    std::cout << "Number of iterations: " << it << std::endl;
    std::cout << "The minimum is (" << X1 << " ; " << X2 << ")" << std::endl;

    return 0;
}

double derivativeX1(const double &x)
{
    return 2*(x + 4);
}

double derivativeX2(const double &x)
{
    return 24*(x - 10);
}
