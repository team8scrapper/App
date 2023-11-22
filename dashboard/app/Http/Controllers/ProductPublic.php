<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use App\Models\Product;
use App\Models\ProductEntry;
use Illuminate\Support\Facades\Auth;
use Carbon\Carbon;

class ProductPublic extends Controller
{
    public function index(Request $request)
    {
        $query = "";
        $capacity = [];
        if ($request->has('query'))
            $query = $request['query'];

        $products = Product::where('name', 'like', '%'.$query.'%')->orWhere('id', 'like', $query.'%')->get();
        
        return Inertia::render('Products/Index', [
            'products' => $products,
            'admin' => false,
            'query' => $query,
            'capacity' => $capacity,
        ]);
    }

    public function show(Product $product)
    {
        return Inertia::render('Products/Show', [
            'product' => $product->load(['product_entries' => function ($query) {
                $query->whereDate('created_at', Carbon::today())->orderBy('created_at', 'DESC')->with('store')->get();
            } ]),

            'history' => ProductEntry::with('store')->where('product_id', $product->id)->get(),
        ]);
    }
}