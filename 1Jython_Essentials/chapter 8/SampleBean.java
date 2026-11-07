public class SampleBean {
    
    public SampleBean() {
        this._integerProperty = 0;
        this._stringProperty = "initialized";
    }
    
    private int _integerProperty;
    
    public int getIntegerProperty() { 
        return this._integerProperty; 
    }
    
    public void setIntegerProperty(int i) { 
        this._integerProperty = i;
    }
    
    private String _stringProperty;
    
    public String getStringProperty() { 
        return this._stringProperty;
    }
    
    public void setStringProperty(String s) {
        this._stringProperty = s;
    }
    
}

