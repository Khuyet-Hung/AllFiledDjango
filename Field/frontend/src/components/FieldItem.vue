<template>
    <div v-if="filedProps.type === 'checkbox'" class="form-group">
        <h2>{{filedProps}}</h2>
        <div class="form-check form-check-inline">
            <input :type="filedProps.type" class="form-check-input form-control-field" 
                    :name="filedProps.name" 
                    :id="'id_'+filedProps.name"
                    :disabled="filedProps.disabled"
                    :required="filedProps.required" />
            <label class="form-check-label" 
                    :for="'id_'+filedProps.name">{{filedProps.label}}</label>
        </div>
        <small class="form-text text-muted"> {{filedProps.help_text}} </small>
        <div class="valid-feedback">
            Hoàn thành
        </div>
        <div class="invalid-feedback" 
            :id="'err_mess_id_' + filedProps.name">
        </div>
    </div>
    <!-- ////////////////////////////////////////////////////////////////////////// -->
    <div v-else-if="filedProps.type === 'select'" class="form-group">
        <h2>{{filedProps}}</h2>
        <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
        <select :name="filedProps.name"
                :disabled="filedProps.disabled"
                :maxlength="filedProps.maxlength"
                :required="filedProps.required" class="form-control form-control-field" 
                :id="'id_'+filedProps.name"
                :multiple="filedProps.multiple" >
            <option v-for="option in filedProps.choices" :key="option.id"
                    :value="option[0]">{{option[1]}}</option>
        </select>
        <div class="valid-feedback">
            Hoàn thành
        </div>
        <div class="invalid-feedback" 
            :id="'err_mess_id_' + filedProps.name">
        </div>
        <small class="form-text text-muted"> {{filedProps.help_text}} </small>
    </div>
    <!-- ////////////////////////////////////////////////////////////////////////// -->
    <div v-else-if="filedProps.type === 'textarea'" class="form-group">
        <h2>{{filedProps}}</h2>
        <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
        <textarea class="form-control form-control-field"
                :id="'id_'+filedProps.name" 
                :maxlength="filedProps.maxlength"
                :max="filedProps.max"
                :min="filedProps.min"
                :name="filedProps.name"
                :disabled="filedProps.disabled"
                :required="filedProps.required"
                :placeholder="filedProps.verbose_name" 
                :cols="filedProps.cols" 
                :rows="filedProps.rows"></textarea>
        <div class="valid-feedback">
            Hoàn thành
        </div>
        <div class="invalid-feedback" 
            :id="'err_mess_id_' + filedProps.name">
        </div>
        <small class="form-text text-muted"> {{filedProps.help_text}} </small>
    </div>
    <!-- ////////////////////////////////////////////////////////////////////////// -->
    <div v-else-if="filedProps.type === 'file'" class="form-group">
        <h2>{{filedProps}}</h2>
        <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
        <div class="custom-file"> 
            <input class="form-control form-control-field" 
                    :accept="filedProps.accept" 
                    :type="filedProps.type"  
                    :name="filedProps.name" 
                    :id="'id_'+filedProps.name" 
                    :disabled="filedProps.disabled"
                    :required="filedProps.required"
                    :aria-describedby="filedProps.name" /> 
        </div>
        <div class="valid-feedback">
            Hoàn thành
        </div>
        <div class="invalid-feedback" 
            :id="'err_mess_id_' + filedProps.name">
        </div>
        <small class="form-text text-muted">
            {{filedProps.help_text}}
        </small>
    </div>
    <!-- ////////////////////////////////////////////////////////////////////////// -->

    <div v-else-if="filedProps.type === 'datetime'" class="form-group">
        <div class="row">
            <div class="col-6">
                <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
                <input class="form-control form-control-field" type="time"
                        :id="'id_'+filedProps.name" 
                        :required="filedProps.required"
                        :disabled="filedProps.disabled"
                        :name="filedProps.name"/>
                <small class="form-text text-muted"> {{filedProps.help_text}} </small>
                <div class="valid-feedback">
                    Hoàn thành
                </div>
                <div class="invalid-feedback" :id="'err_mess_id_' + filedProps.name">
        </div>
            </div>

            <div class="col-6">
                <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
                <input class="form-control form-control-field" type="date"
                        :id="'id_'+filedProps.name" 
                        :required="filedProps.required"
                        :disabled="filedProps.disabled"
                        :name="filedProps.name"/>
                <small class="form-text text-muted"> {{filedProps.help_text}} </small>
                <div class="valid-feedback">
                    Hoàn thành
                </div>
            </div>
        </div>
    </div>
    <!-- ////////////////////////////////////////////////////////////////////////// -->
    <div v-else class="form-group">
        <h2>{{filedProps}}</h2>
        <label :for="'id_'+filedProps.name">{{filedProps.label}} </label>
        <input :id="'id_'+filedProps.name" 
                :type="filedProps.type" 
                :maxlength="filedProps.maxlength"
                :max="filedProps.max"
                :min="filedProps.min"
                :name="filedProps.name"
                :disabled="filedProps.disabled"
                :required="filedProps.required"
                :placeholder="filedProps.verbose_name"
                :step="(filedProps.step === null ? '' : filedProps.step)"
                class="form-control form-control-field "/>
        <div class="valid-feedback">
            Hoàn thành
        </div>
        <div class="invalid-feedback" 
            :id="'err_mess_id_' + filedProps.name">
        </div>
        <small class="form-text text-muted">
            {{filedProps.help_text}}
        </small>
    </div>
</template>

<script>
export default {
    name: "FieldItem",
    props: ["filedProps"],
}
</script>

<style>

</style>