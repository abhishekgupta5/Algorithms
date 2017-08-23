#include<bits/stdc++.h>
using namespace std;

struct Point{
    double x;
    double y;
    };

double cross_product(Point a, Point b){
    return a.x*b.y - b.x*a.y;
    //Area is negative in clockwise dir and positive in counter-clockwise order
    }

double area_of_triangle_origin(Point a, Point b){
    //Area of a triangle with one vertex on origin
    return abs(cross_product(a,b) / 2.0);
    }

double area_of_triangle(Point a, Point b, Point c){
    return abs((cross_product(a,b)+cross_product(b,c) + cross_product(c,a)) / 2.0)
    }

double area_of_polygon(Point[] vertices, int n){
    double sum = 0.0;
    for (int i=0; i<n; i++){
        sum += cross_product(vertices[i],vertices[i+1]%n);
        }
    return abs(sum)/2.0;
    }

