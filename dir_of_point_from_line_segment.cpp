# include<bits/stdc++.h>
using namespace std;

const int LEFT = -1, RIGHT = +1, ON_THE_LINE = 0;

struct Point{
    double x, y;
    };

double get_cross_product(Point p1, Point p2){
    return p1.x*p2.y - p1.y*p2.x;
    }

Point subtract(Point p1, Point p2){
    //Trasform coordinates of p1 wrt p2 as origin
    Point result;
    result.x = p1.x-p2.x;
    result.y = p1.y-p2.y;
    return result;
    }

int get_direction(Point a, Point b, Point p){
    //First transform 'b', 'p' wrt 'a' as origin
    b = subtract(b, a);
    p = subtract(p, a);
    double cross_product = get_cross_product(b, p);
    if (cross_product > 0)
        return LEFT;
    else if (cross_product < 0)
        return RIGHT;
    else return ON_THE_LINE;
    }

main(){
    Point a;
    a.x = 12.2;
    a.y = 29.8;

    Point b;
    b.x = -1.8;
    b.y = 6.8;

    Point c;
    c.x = 3.9;
    c.y = -7.9;

    int answer = get_direction(Point a, Point b, Point c);

    }
