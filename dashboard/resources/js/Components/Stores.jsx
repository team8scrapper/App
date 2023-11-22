import React from "react";
import { router } from "@inertiajs/react";
import dayjs from "dayjs";

// import deleteDialog from "@/Components/DeleteDialog";

export default function Stores({ stores, admin }) {
    // const deleteStore = (storeId) => {
    //     deleteDialog(
    //         `/stores/${storeId}`,
    //         "Are you sure you want to delete this store?"
    //     );
    // };
    return (
        <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table className="w-full text-sm text-left text-gray-500">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" className="px-6 py-3">
                            ID
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Name
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Image
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Action
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {stores.map((store) => (
                        <tr key={store.id} className="bg-white border-b">
                            <th
                                scope="row"
                                className="px-6 py-4 whitespace-nowrap"
                            >
                                {store.id}
                            </th>
                            <td className="px-6 font-medium text-gray-900 py-4">
                                {store.name}
                            </td>
                            <td className="px-6 font-medium text-gray-900 py-4">
                                <img src={store.logo_url} />
                            </td>
                            <td className="px-6 py-4">
                                {admin && (
                                    <>
                                        <a
                                            href={route(
                                                "admin.stores.edit",
                                                store.id
                                            )}
                                            className="font-medium text-blue-600 hover:underline mr-2"
                                        >
                                            Edit
                                        </a>
                                        <button
                                            onClick={() =>
                                                deleteStore(store.id)
                                            }
                                            className="font-medium text-red-600 hover:underline"
                                        >
                                            Delete
                                        </button>
                                    </>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
