public class IndexBean {
    
    public IndexBean() {
        this._arrayProperty = new String[] {"Zero", "One", "Twp"};
    }
    
    private String[] _arrayProperty;
    
    public String[] getArrayProperty() {
        return this._arrayProperty;
    }
    
    public void setArrayProperty(String[] ar) {
        this._arrayProperty = ar;
    }
   
}

