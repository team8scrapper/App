import "./bootstrap";
import "../css/app.css";
import "dayjs/locale/pt";

import dayjs from "dayjs";
import { createRoot } from "react-dom/client";
import { createInertiaApp } from "@inertiajs/react";
import { resolvePageComponent } from "laravel-vite-plugin/inertia-helpers";
import { ToastContainer } from "react-toastify";

import "react-toastify/dist/ReactToastify.css";

const appName = import.meta.env.VITE_APP_NAME || "Laravel";

createInertiaApp({
    title: (title) => `${title} - ${appName}`,
    resolve: (name) =>
        resolvePageComponent(
            `./Pages/${name}.jsx`,
            import.meta.glob("./Pages/**/*.jsx")
        ),
    setup({ el, App, props }) {
        const root = createRoot(el);

        root.render(
            <>
                <App {...props} />
                <ToastContainer />
            </>
        );
    },
    progress: {
        color: "#4B5563",
    },
});
