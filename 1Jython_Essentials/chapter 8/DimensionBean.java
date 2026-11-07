import java.awt.Dimension;

public class DimensionBean {
    
    public DimensionBean() {
        this._dimProperty = new Dimension(0, 0);
    }
    
    private Dimension _dimProperty;
    
    public Dimension getDimensionProperty() {
        return this._dimProperty;
    }
    
    public void setDimensionProperty(Dimension d) {
        this._dimProperty = d;
    }
   
}

