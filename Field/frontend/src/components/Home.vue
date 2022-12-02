<template class="home">
    <form @submit.prevent="postAllFiled()"
            id="field-form" enctype="multipart/form-data">
        <FieldItem v-for="item in fields" :key="item.id" :filedProps="item"/>
        <button type="submit" class="btn btn-primary">OK</button>
    </form>
</template>

<script>
import FieldItem from './FieldItem'
import { ref } from "vue";
import axios from 'axios'
export default {
    name: "Home",
    components: {
        FieldItem
    },
    setup() {
        const fields = ref([]);

        const getAllFiled= async() => {
            try {
                const res = await axios.get('http://localhost:8000/api/')
                fields.value = res.data
            } catch (error) {
                console.log("error", error)
            }
        }
        getAllFiled()

        // Supmit form////////////////////////////////////////////////////////////////////
        const postAllFiled = async() => {
            var form = document.getElementById('field-form');
            var formData = new FormData(form);
            await axios.post(`http://localhost:8000/api/`, formData).then(response => {
                var inputs = document.querySelectorAll('.form-control-field')
                // lập qua từng input 
                for (var input of inputs) {
                    // xóa giá trị error và gắn giá trị success cho mỗi input
                    input.classList.remove('is-invalid')
                    input.classList.add('is-valid')
                        // lập qua từng phần tử của các lỗi được server trả về
                    for (var resp in response.data) {
                        // kiểm tra các tên của input có nằm trong danh sách các phần tử error được trả về hay k
                        if (resp === input.name) {
                            // nếu có thì xóa giá trị success cho input và gắn giá trị error
                            input.classList.remove('is-valid')
                            input.classList.add('is-invalid')
                                // gắn error message cho các input lỗi
                            document.querySelectorAll(`#err_mess_id_${resp}`)[0].innerText = response.data[resp]
                        }
                    }
                }
            }).catch((errors) => {
                console.log(errors)
            });
        }
        return { fields, postAllFiled};
    },
};
</script>

<style scoped>

</style>