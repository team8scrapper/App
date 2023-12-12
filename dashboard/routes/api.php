<?php

use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StoreController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});


Route::post('/test_store', function (Request $request) {

    $data = [
        "name" => $request['name'],
        "search_url" => $request['search_url'],
        "logo_url" => $request['logo_url'],
        "currency" => $request['currency'],
        "use_generic" => $request['use_generic'],
        "base_url" => $request['base_url'],
        "redirected" => $request['redirected'],
        "results_classes" => $request['results_classes'],
        "name_classes" => $request['name_classes'],
        "price_classes" => $request['price_classes'],
        "testing_ean" => $request['testing_ean'],
    ];

    return $data;

    // return $request['testing_ean'];
    $response = Http::withHeaders([
        'Access-Control-Allow-Origin' => '*',
        "Content-Type" => "application/json",
        "Access-Control-Allow-Methods" => "GET,PUT,POST,DELETE,PATCH,OPTIONS",
        "Access-Control-Allow-Headers" => "append,delete,entries,foreach,get,has,keys,set,values,Authorization",
    ])->post('http://127.0.0.1:4242/test', $data);
    
    // $body = $response->body();

    return $response->body();
});

Route::get('/test', function (Request $request) {
    return "test";
});