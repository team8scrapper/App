import React from "react";
import { Link, usePage } from "@inertiajs/react";

export default function YearsNavigation({ availableYears }) {
    const { url } = usePage();

    return (
        <div>
            <Link
                replace
                preserveScroll
                // preserveState
                href={`?year=`}
                className={`cursor-pointer mx-1 inline-flex items-center px-4 py-2 bg-white border border-gray-300 rounded-md font-semibold text-xs text-gray-700 uppercase tracking-widest shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-500 focus:ring-offset-2 disabled:opacity-25 transition ease-in-out duration-150  ${
                    (url.endsWith("=") || !url.includes("?year=")) &&
                    "bg-amber-800 hover:bg-amber-900 border-amber-800 text-white"
                }`}
            >
                All
            </Link>
            {Boolean(availableYears.length) &&
                availableYears.map((year) => (
                    <Link
                        key={year}
                        replace
                        preserveScroll
                        // preserveState
                        href={`?year=${year}`}
                        className={`cursor-pointer mx-1 inline-flex items-center px-4 py-2 bg-white border border-gray-300 rounded-md font-semibold text-xs text-gray-700 uppercase tracking-widest shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-500 focus:ring-offset-2 disabled:opacity-25 transition ease-in-out duration-150  ${
                            url.includes(`?year=${year}`) &&
                            "bg-amber-800 hover:bg-amber-900 border-amber-800 text-white"
                        }`}
                    >
                        {year}
                    </Link>
                ))}
        </div>
    );
}
