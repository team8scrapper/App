<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Store extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'search_url',
        'logo_url',
        'use_generic',
        'base_url',
        'results_classes',
        'name_classes',
        'price_classes',
        'redirected',
        'currency',
    ];

    public function product_entries(): HasMany
    {
        return $this->hasMany(ProductEntry::class);
    }
}