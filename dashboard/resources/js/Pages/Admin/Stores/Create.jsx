import React, { useState } from "react";
import AuthenticatedLayout from "@/Layouts/AuthenticatedLayout";
import InputError from "@/Components/InputError";
import InputLabel from "@/Components/InputLabel";
import TextInput from "@/Components/TextInput";
import PrimaryButton from "@/Components/PrimaryButton";
import Checkbox from "@/Components/Checkbox";
import SecondaryButton from "@/Components/SecondaryButton";
import { useForm, Head, router } from "@inertiajs/react";
import { IoIosAlert } from "react-icons/io";
import { IoIosCheckmarkCircle } from "react-icons/io";
import { AiOutlineLoading3Quarters } from "react-icons/ai";
import { toast } from "react-toastify";

import { getTestData } from "@/Pages/Admin/Stores/Edit";

export default function Create({ auth }) {
    // const [testCount, setTestCount] = useState(0);
    // const [validStore, setValidStore] = useState(false);
    const [loading, setLoading] = useState(false);
    const [testingRes, setTestingRes] = useState("");
    const {
        data,
        setData,
        post,
        processing,
        reset,
        errors,
        clearErrors,
        setError,
    } = useForm({
        name: "",
        search_url: "",
        logo_url: "",
        use_generic: false,
        base_url: "",
        results_classes: "",
        name_classes: "",
        price_classes: "",
        testing_ean: "",
    });

    const testStore = async () => {
        console.log("test store");
        clearErrors();
        if (!data.testing_ean) {
            setError("testing_ean", "You need to enter a search term");
            return;
        }
        setLoading(true);
        setTestingRes("");
        const res = await getTestData(data);
        console.log(res);
        setTestingRes(JSON.stringify(res, null, 4));
        setLoading(false);
    };

    const submit = (e) => {
        e.preventDefault();
        post(route("admin.stores.store"), {
            onSuccess: () => {
                toast.success("Store added successfully.");
                reset();
            },
            onError: () => {
                toast.error("Error adding a store!");
            },
        });
    };

    return (
        <AuthenticatedLayout
            user={auth.user}
            header={
                <div className="flex justify-between">
                    <h2 className="font-semibold text-xl text-gray-800 leading-tight">
                        New Store
                    </h2>
                </div>
            }
        >
            <Head title="New Store" />

            <div className="max-w-2xl mx-auto p-4 sm:p-6 lg:p-8">
                <SecondaryButton
                    type="button"
                    className="mb-6"
                    onClick={() => router.get("/admin/stores")}
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="w-4 h-4 mr-1"
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75"
                        />
                    </svg>
                    Back
                </SecondaryButton>

                <div className="p-4 sm:p-8 bg-white shadow rounded-lg">
                    <header>
                        <h2 className="text-lg font-medium text-gray-900">
                            Register a new Store
                        </h2>
                    </header>

                    <form onSubmit={submit} className="mt-6 space-y-6">
                        <div>
                            <InputLabel htmlFor="name" value="Name" />

                            <TextInput
                                id="name"
                                type="text"
                                name="name"
                                value={data.name}
                                className="mt-1 block w-full"
                                onChange={(e) =>
                                    setData("name", e.target.value)
                                }
                            />

                            <InputError
                                message={errors.name}
                                className="mt-2"
                            />
                        </div>

                        <div>
                            <InputLabel
                                htmlFor="search_url"
                                value="Search URL"
                            />

                            <TextInput
                                id="search_url"
                                type="text"
                                name="search_url"
                                value={data.search_url}
                                className="mt-1 block w-full"
                                onChange={(e) =>
                                    setData("search_url", e.target.value)
                                }
                            />

                            <InputError
                                message={errors.search_url}
                                className="mt-2"
                            />
                        </div>

                        <div>
                            <InputLabel htmlFor="logo_url" value="Logo URL" />

                            <TextInput
                                id="logo_url"
                                type="text"
                                name="logo_url"
                                value={data.logo_url}
                                className="mt-1 block w-full"
                                onChange={(e) =>
                                    setData("logo_url", e.target.value)
                                }
                            />

                            <InputError
                                message={errors.logo_url}
                                className="mt-2"
                            />
                        </div>

                        <div className="block mt-4">
                            <label className="flex items-center">
                                <Checkbox
                                    name="use_generic"
                                    checked={data.use_generic}
                                    onChange={(e) =>
                                        setData("use_generic", e.target.checked)
                                    }
                                />
                                <span className="ml-2 text-sm text-gray-600">
                                    Use Generic Scrapper
                                </span>
                            </label>
                        </div>

                        {Boolean(data.use_generic) && (
                            <>
                                <div>
                                    <InputLabel
                                        htmlFor="base_url"
                                        value="Base URL"
                                    />

                                    <TextInput
                                        id="base_url"
                                        type="text"
                                        name="base_url"
                                        value={data.base_url}
                                        className="mt-1 block w-full"
                                        onChange={(e) =>
                                            setData("base_url", e.target.value)
                                        }
                                    />
                                    <p className="mt-1 text-sm text-gray-600">
                                        The website base URL. eg:
                                        https://www.continente.pt
                                    </p>

                                    {/* TODO remove trailing slash from base url if user inserts it */}

                                    <InputError
                                        message={errors.base_url}
                                        className="mt-2"
                                    />
                                </div>

                                <div>
                                    <InputLabel
                                        htmlFor="results_classes"
                                        value="Results Classes"
                                    />

                                    <TextInput
                                        id="results_classes"
                                        type="text"
                                        name="results_classes"
                                        value={data.results_classes}
                                        className="mt-1 block w-full"
                                        onChange={(e) =>
                                            setData(
                                                "results_classes",
                                                e.target.value
                                            )
                                        }
                                    />

                                    <InputError
                                        message={errors.results_classes}
                                        className="mt-2"
                                    />
                                </div>

                                <div>
                                    <InputLabel
                                        htmlFor="name_classes"
                                        value="Name Classes"
                                    />

                                    <TextInput
                                        id="name_classes"
                                        type="text"
                                        name="name_classes"
                                        value={data.name_classes}
                                        className="mt-1 block w-full"
                                        onChange={(e) =>
                                            setData(
                                                "name_classes",
                                                e.target.value
                                            )
                                        }
                                    />

                                    <InputError
                                        message={errors.name_classes}
                                        className="mt-2"
                                    />
                                </div>

                                <div>
                                    <InputLabel
                                        htmlFor="price_classes"
                                        value="Price Classes"
                                    />

                                    <TextInput
                                        id="price_classes"
                                        type="text"
                                        name="price_classes"
                                        value={data.price_classes}
                                        className="mt-1 block w-full"
                                        onChange={(e) =>
                                            setData(
                                                "price_classes",
                                                e.target.value
                                            )
                                        }
                                    />

                                    <InputError
                                        message={errors.price_classes}
                                        className="mt-2"
                                    />
                                </div>

                                <div>
                                    <div>
                                        <InputLabel
                                            htmlFor="testing_ean"
                                            value="Testing EAN"
                                        />

                                        <TextInput
                                            id="testing_ean"
                                            type="text"
                                            name="testing_ean"
                                            value={data.testing_ean}
                                            className="mt-1 block w-full"
                                            onChange={(e) =>
                                                setData(
                                                    "testing_ean",
                                                    e.target.value
                                                )
                                            }
                                        />

                                        <InputError
                                            message={errors.testing_ean}
                                            className="mt-2"
                                        />
                                    </div>

                                    <PrimaryButton
                                        type="button"
                                        className="mt-4 mr-2"
                                        onClick={() => testStore()}
                                        disabled={loading}
                                    >
                                        Test Store
                                    </PrimaryButton>
                                    {Boolean(loading) && (
                                        <AiOutlineLoading3Quarters className="animate-spin inline-block" />
                                    )}
                                    {Boolean(testingRes) && (
                                        <div className="bg-gray-200 p-4 rounded-lg mt-4 whitespace-pre overflow-x-auto">
                                            <code className="">
                                                {testingRes}
                                            </code>
                                        </div>
                                    )}
                                </div>
                            </>
                        )}

                        <div className="flex justify-end">
                            <SecondaryButton
                                type="button"
                                className="mt-4 mr-2"
                                onClick={() => router.get("/admin/stores")}
                            >
                                Cancelar
                            </SecondaryButton>
                            <PrimaryButton
                                className="mt-4"
                                disabled={processing}
                            >
                                Add Store
                            </PrimaryButton>
                        </div>
                    </form>
                </div>
            </div>
        </AuthenticatedLayout>
    );
}
