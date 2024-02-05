import { generateClasses } from "@formkit/themes";



const config = {
    config: {
        classes: generateClasses({
            global: {
                form: 'flex flex-col gap-8',
                wrapper: 'flex flex-col gap-2',
                message: 'text-sm font-bold text-red-400 mt-2',
                label: '',
                input: 'w-full px-4 py-1 outline outline-1 outline-gray-200 rounded-sm text-gray-600'
            },
            submit: {
                input: ' $reset px-4 py-2 bg-indigo-500 rounded-md text-white font-semibold'
            }
        })
    }
}

export default config;
